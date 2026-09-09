#!/usr/bin/env python3
"""Regenerate the six content diagrams (EN + VI) with collision-safe layouts.

Rules:
- wrap() splits on newlines first, then word-wraps with a conservative width.
- Text is top-anchored at explicit baselines (no vertical centering of
  variable-height blocks inside fixed boxes).
- Icon markers and text never share a band; badges sit above boxes.
- Canvas height is computed from the rendered content.
"""
import html, os

FONT = "system-ui, -apple-system, 'Segoe UI', Roboto, Arial, sans-serif"
INK = '#0f172a'; SUB = '#475569'; LINE = '#cbd5e1'
BLUE = '#2563eb'; GREEN = '#16a34a'; RED = '#dc2626'; AMBER = '#d97706'

def esc(s): return html.escape(s, quote=False)

def wrap(text, size, maxw):
    """Split on newlines first, then word-wrap. Returns list of lines."""
    out = []
    for para in text.split('\n'):
        words = para.split(' ')
        cur = ''
        for wd in words:
            cand = (cur + ' ' + wd).strip()
            if _w(cand, size) <= maxw or not cur:
                cur = cand
            else:
                out.append(cur); cur = wd
        if cur:
            out.append(cur)
    return out

def _w(s, size):
    # conservative ~0.60em average; over-estimating width only wastes space
    return sum(0.60 * size for c in s)

def put_top(lines, x, y0, size, fill=INK, anchor='start', lh=None, weight='normal', mono=False):
    lh = lh or size * 1.25
    fam = '"SFMono-Regular", Menlo, Consolas, monospace' if mono else FONT
    out = []
    for i, ln in enumerate(lines):
        yy = y0 + i * lh
        out.append(f'<text x="{x:.0f}" y="{yy:.0f}" text-anchor="{anchor}" font-family="{fam}" '
                   f'font-size="{size}" font-weight="{weight}" fill="{fill}">{esc(ln)}</text>')
    return ''.join(out)

def center(text, cx, y, size, fill=INK, weight='normal'):
    return (f'<text x="{cx:.0f}" y="{y:.0f}" text-anchor="middle" font-family="{FONT}" '
            f'font-size="{size}" font-weight="{weight}" fill="{fill}">{esc(text)}</text>')

def rrect(x, y, w, h, rx, fill='#ffffff', stroke=LINE, sw=1.5):
    return (f'<rect x="{x:.0f}" y="{y:.0f}" width="{w:.0f}" height="{h:.0f}" rx="{rx}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')

def hline(x1, x2, y, color=SUB, sw=2, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<line x1="{x1:.0f}" y1="{y:.0f}" x2="{x2:.0f}" y2="{y:.0f}" stroke="{color}" stroke-width="{sw}"{d}/>'

def vline(x, y1, y2, color=SUB, sw=2, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<line x1="{x:.0f}" y1="{y1:.0f}" x2="{x:.0f}" y2="{y2:.0f}" stroke="{color}" stroke-width="{sw}"{d}/>'

def arrow_right(x1, x2, y, color=SUB, sw=3):
    return (hline(x1, x2 - 13, y, color, sw) +
            f'<polygon points="{x2:.0f},{y:.0f} {x2-13:.0f},{y-7:.0f} {x2-13:.0f},{y+7:.0f}" fill="{color}"/>')

def arrow_up(x, y_base, y_tip, color=SUB, sw=3):
    return (vline(x, y_base, y_tip + 4, color, sw) +
            f'<polygon points="{x:.0f},{y_tip:.0f} {x-8:.0f},{y_base:.0f} {x+8:.0f},{y_base:.0f}" fill="{color}"/>')

def badge(cx, cy, r, num):
    return (f'<circle cx="{cx:.0f}" cy="{cy:.0f}" r="{r}" fill="{BLUE}"/>' +
            center(num, cx, cy + 6, 16, '#ffffff', '700'))

def check(x, y, color=GREEN, s=1.0):
    return (f'<path d="M {x-10*s:.0f} {y:.0f} l {6*s:.0f} {6*s:.0f} l {12*s:.0f} -{14*s:.0f}" '
            f'stroke="{color}" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')

def cross(x, y, color=RED, s=1.0):
    return (f'<path d="M {x-9*s:.0f} {y-9*s:.0f} L {x+9*s:.0f} {y+9*s:.0f} '
            f'M {x+9*s:.0f} {y-9*s:.0f} L {x-9*s:.0f} {y+9*s:.0f}" stroke="{color}" '
            f'stroke-width="4" stroke-linecap="round"/>')

def svg(w, h, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.0f} {h:.0f}" '
            f'role="img" font-family="{FONT}">\n{body}</svg>\n')

# --------------------------------------------------------------------------
# 1) Evaluation loop --------------------------------------------------------
# --------------------------------------------------------------------------
def eval_loop(lang):
    if lang == 'en':
        labels = [("Define “good”", "outputs"), ("Collect", "examples"),
                  ("Run model", "& score"), ("Inspect", "failures"),
                  ("Improve", "& rerun")]
        ret = 'repeat until failures stop shrinking'
    else:
        labels = [("Định nghĩa", "“tốt” là gì"), ("Thu thập", "ví dụ mẫu"),
                  ("Chạy mô hình", "& chấm điểm"), ("Xem & phân", "loại lỗi"),
                  ("Cải thiện", "& chạy lại")]
        ret = 'lặp lại đến khi lỗi không còn giảm'

    W = 880
    bw, gap, n = 156, 20, len(labels)
    x0 = (W - (n * bw + (n - 1) * gap)) / 2
    y0, bh = 96, 100
    b = []
    cx = []
    for i, (a, c) in enumerate(labels):
        x = x0 + i * (bw + gap)
        cx.append(x + bw / 2)
        b.append(rrect(x, y0, bw, bh, 18, '#ffffff', BLUE, 2))
        b.append(badge(x + bw / 2, y0 - 24, 15, str(i + 1)))
        # two lines, top-anchored, comfortably inside the box
        b.append(put_top([a, c], x + bw / 2, y0 + 40, 17, INK, 'middle', lh=24, weight='600'))
        if i < n - 1:
            b.append(arrow_right(x + bw, x + bw + gap, y0 + bh / 2, SUB))
    # return arrow
    yret = 238
    b.append(hline(cx[-1], cx[0], yret, SUB, 3, dash='7 6'))
    b.append(arrow_up(cx[0], yret, y0 + bh + 12, SUB))
    b.append(center(ret, W / 2, 274, 19, SUB, '600'))
    H = 300
    return svg(W, H, ''.join(b))

# --------------------------------------------------------------------------
# 2) Scorecard --------------------------------------------------------------
# --------------------------------------------------------------------------
def scorecard(lang):
    if lang == 'en':
        hdr = ['Test case', 'What “good” looks like', 'Score', 'Pass?']
        rows = [
            ("Answer a policy question using HR documents", "Correct and cites the source", "5"),
            ("Summarize meeting notes into three bullets", "Three bullets, nothing invented", "4"),
            ("Output JSON that our parser accepts", "Valid and matches the schema", "5"),
            ("The documents do not contain the answer", "Admits it — no guessing", "2"),
        ]
    else:
        hdr = ['Ca kiểm thử', 'Thế nào là “tốt”', 'Điểm', 'Đạt?']
        rows = [
            ("Trả lời câu hỏi chính sách từ tài liệu nhân sự", "Đúng và có trích nguồn", "5"),
            ("Tóm tắt biên bản họp thành 3 gạch đầu dòng", "3 gạch đầu dòng, không bịa đặt", "4"),
            ("Xuất JSON mà hệ thống phân tích được", "Hợp lệ, đúng cấu trúc", "5"),
            ("Tài liệu không chứa câu trả lời", "Thừa nhận “không biết”", "2"),
        ]

    W = 880
    cols = [320, 300, 100, 100]           # widths
    x0 = (W - sum(cols)) / 2
    hh = 46
    fsize = 17
    lh = 22
    top = 40

    def colx(i): return x0 + sum(cols[:i])

    # pre-wrap to know line counts
    wrapped = []
    for case, ideal, score in rows:
        wrapped.append((wrap(case, fsize, cols[0] - 24),
                        wrap(ideal, fsize, cols[1] - 24)))
    rows_h = [max(len(c), len(i)) for c, i in wrapped]
    rh_base = 60
    y = top + hh
    row_y = []
    for rh in rows_h:
        row_y.append(y)
        y += max(rh_base, rh * lh + 30)

    def row_bottom(i):
        return (row_y[i + 1] if i + 1 < len(row_y) else y) - 4

    H = y + 20
    b = []
    b.append(rrect(x0, top, sum(cols), H - top - 8, 14, '#f1f5f9', LINE, 1))
    for i, htext in enumerate(hdr):
        b.append(center(htext, colx(i) + cols[i] / 2, top + hh / 2 + 6, 19, INK, '700'))
    for ri, (case, ideal, score) in enumerate(rows):
        yy = row_y[ri]
        rh_row = row_bottom(ri) - yy
        b.append(rrect(x0, yy, sum(cols), rh_row, 0,
                       '#ffffff' if ri % 2 == 0 else '#f8fafc', '#e2e8f0', 1))
        b.append(put_top(wrapped[ri][0], colx(0) + 14, yy + 18, fsize, INK, lh=lh, weight='500'))
        b.append(put_top(wrapped[ri][1], colx(1) + 14, yy + 18, fsize, INK, lh=lh, weight='500'))
        sc = int(score)
        col = GREEN if sc >= 4 else (AMBER if sc == 3 else RED)
        b.append(center(score, colx(2) + cols[2] / 2, yy + rh_row / 2 + 9, 26, col, '800'))
        b.append(check(colx(3) + cols[3] / 2, yy + rh_row / 2) if sc >= 4
                 else cross(colx(3) + cols[3] / 2, yy + rh_row / 2))
    return svg(W, H, ''.join(b))

# --------------------------------------------------------------------------
# 3) RAG architecture -------------------------------------------------------
# --------------------------------------------------------------------------
def rag_arch(lang):
    if lang == 'en':
        stages = [("Embed the", "question"), ("Search top-k", "in your documents"),
                  ("Context", "into the prompt"), ("Answer", "+ cite sources")]
        note = 'your documents · vector store'
        chunks = 'top-k retrieved chunks'
        cite = '[1] page 3'
    else:
        stages = [("Nhúng câu hỏi", "thành vector"), ("Tìm top-k", "trong tài liệu"),
                  ("Đưa ngữ cảnh", "vào prompt"), ("Trả lời", "+ trích nguồn")]
        note = 'tài liệu của bạn · vector store'
        chunks = 'các đoạn top-k lấy được'
        cite = '[1] trang 3'

    W = 880
    bw, gap, n = 170, 16, len(stages)
    x0 = (W - (n * bw + (n - 1) * gap)) / 2
    y0, bh = 150, 104
    cy = y0 + bh / 2
    xs = [x0 + i * (bw + gap) + bw / 2 for i in range(n)]
    b = []
    for i, (a, c) in enumerate(stages):
        x = x0 + i * (bw + gap)
        b.append(rrect(x, y0, bw, bh, 18, '#ffffff', BLUE, 2))
        b.append(badge(xs[i], y0 - 26, 15, str(i + 1)))
        b.append(put_top([a, c], xs[i], y0 + 52, 17, INK, 'middle', lh=24, weight='600'))
        if i < n - 1:
            b.append(arrow_right(x + bw, x + bw + gap, y0 + bh / 2, SUB))

    yb = y0 + bh
    band_y = yb + 34
    # docs note under stage 2
    nx, nw = xs[1], 260
    b.append(vline(xs[1], yb + 8, band_y - 4, AMBER, 2, dash='4 4'))
    b.append(rrect(nx - nw / 2, band_y, nw, 44, 12, '#fffbeb', AMBER, 1.5))
    b.append(center(note, nx, band_y + 27, 17, AMBER, '600'))
    # answer chip under stage 4
    ax, aw = xs[3], 200
    b.append(rrect(ax - aw / 2, band_y, aw, 44, 22, '#f0fdf4', GREEN, 2))
    b.append(center(cite, ax, band_y + 27, 19, GREEN, '700'))
    # top-k chunk pills under the middle gap (between stage 2 and 3)
    pills = ['...', 'chunk', '...'] if lang == 'en' else ['...', 'đoạn', '...']
    pw, pg, ph = 110, 16, 44
    mid = (xs[1] + xs[2]) / 2
    py = band_y + 72
    total = pw * 3 + pg * 2
    for i, t in enumerate(pills):
        px = mid - total / 2 + i * (pw + pg)
        b.append(rrect(px, py, pw, ph, 10, '#e0e7ff', '#c7d2fe', 1))
        b.append(center(t, px + pw / 2, py + ph / 2 + 6, 16, '#3730a3', '600'))
    b.append(center(chunks, mid, py + ph + 26, 17, SUB, '600'))
    H = py + ph + 52
    return svg(W, H, ''.join(b))

# --------------------------------------------------------------------------
# 4) Closed book vs open book ----------------------------------------------
# --------------------------------------------------------------------------
def open_book(lang):
    if lang == 'en':
        left = ("Closed book — model alone",
                ["Answers only from memory",
                 "Knowledge stops at the training cutoff",
                 "No access to your private documents"], False)
        right = ("Open book — with RAG",
                 ["Model reads the retrieved documents",
                  "Answers are grounded in your data",
                  "It can point to the exact source"], True)
    else:
        left = ("Thi vở đóng — chỉ có mô hình",
                ["Trả lời theo trí nhớ",
                 "Kiến thức dừng ở thời điểm huấn luyện",
                 "Không truy cập tài liệu riêng của bạn"], False)
        right = ("Thi vở mở — có RAG",
                 ["Mô hình đọc các tài liệu đã tra cứu",
                  "Câu trả lời bám vào dữ liệu của bạn",
                  "Có thể chỉ đúng nguồn trích dẫn"], True)

    W = 880
    pw, gap = 400, 24
    x0 = (W - (pw * 2 + gap)) / 2
    y0 = 40
    fsize = 18
    lh = 23

    def panel_height(title, items):
        lines_total = sum(max(1, len(wrap(t, fsize, pw - 110))) for t in items)
        # title band (2 lines max) + items
        return 60 + 44 + lines_total * lh + 4 * 26

    panels = [left, right]
    phs = [panel_height(*p[:2]) for p in panels]
    ph = max(phs)
    H = y0 + ph + 20
    b = []
    for i, (title, items, good) in enumerate(panels):
        x = x0 + i * (pw + gap)
        bg = '#f0fdf4' if good else '#fef2f2'
        bd = '#bbf7d0' if good else '#fecaca'
        b.append(rrect(x, y0, pw, ph, 20, bg, bd, 2))
        b.append(rrect(x + 20, y0 + 22, pw - 40, 60, 12, '#ffffff', bd, 1.5))
        tls = wrap(title, 21, pw - 70)
        b.append(put_top(tls, x + pw / 2, y0 + 44, 21, INK, 'middle', lh=26, weight='800'))
        yy = y0 + 22 + 60 + 26
        for it in items:
            mk = check(x + 36, yy + 6) if good else cross(x + 36, yy + 6)
            b.append(mk)
            ls = wrap(it, fsize, pw - 110)
            b.append(put_top(ls, x + 56, yy, fsize, INK, lh=lh, weight='500'))
            yy += len(ls) * lh + 26
    return svg(W, H, ''.join(b))

# --------------------------------------------------------------------------
# 5) Prompt anatomy ---------------------------------------------------------
# --------------------------------------------------------------------------
def prompt_anatomy(lang):
    if lang == 'en':
        rows = [("Role", "You are a senior editor who reviews drafts."),
                ("Context", "Our product: a note-taking app for students."),
                ("Task", "Rewrite this paragraph to be clear and neutral."),
                ("Format", "Reply with 3 bullets, then a one-line summary."),
                ("Example", "Give one before → after pair to set the style.")]
    else:
        rows = [("Role", "Bạn là biên tập viên kỳ cựu, chuyên rà soát bản nháp."),
                ("Context", "Sản phẩm của chúng tôi: app ghi chú cho sinh viên."),
                ("Task", "Viết lại đoạn này cho rõ ràng và trung lập."),
                ("Format", "Trả lời 3 gạch đầu dòng, rồi 1 dòng tóm tắt."),
                ("Example", "Đưa 1 cặp trước → sau để định hình phong cách.")]
    colors = {'Role': '#7c3aed', 'Context': '#2563eb', 'Task': '#16a34a',
              'Format': '#d97706', 'Example': '#dc2626'}
    W = 880
    x0, cw = 40, 190
    tx = x0 + cw + 14
    tw = W - tx - 40
    y0 = 30
    rh, gap = 60, 22
    b = []
    for i, (label, sample) in enumerate(rows):
        yy = y0 + i * (rh + gap)
        b.append(rrect(x0, yy, cw, rh, 14, colors[label]))
        b.append(center(label, x0 + cw / 2, yy + 38, 20, '#ffffff', '800'))
        b.append(rrect(tx, yy, tw, rh, 14, '#f8fafc', '#e2e8f0', 1))
        ls = wrap(sample, 19, tw - 36)
        b.append(put_top(ls, tx + 20, yy + 20, 19, INK, lh=23, weight='500'))
    H = y0 + len(rows) * (rh + gap) - gap + 24
    return svg(W, H, ''.join(b))

# --------------------------------------------------------------------------
# 6) Weak vs strong prompt (before / after) ---------------------------------
# --------------------------------------------------------------------------
def before_after(lang):
    if lang == 'en':
        weak = ("Weak — vague", "Help me with marketing.",
                "Sure! Marketing is about reaching customers. It is important because…")
        strong = ("Strong — specific",
                  "You are a B2B SaaS copywriter. Write 3 email subject lines for a webinar "
                  "on data security, aimed at IT managers. Keep each under 45 characters, "
                  "no emojis. List them as 1-2-3.",
                  "1) Securing SaaS: what IT must know\n"
                  "2) Data security webinar — IT edition\n"
                  "3) Your stack, your data, their risk")
    else:
        weak = ("Yếu — mơ hồ", "Giúp mình làm marketing với.",
                "Chắc chắn rồi! Marketing là tiếp cận khách hàng. Nó quan trọng vì…")
        strong = ("Mạnh — cụ thể",
                  "Bạn là copywriter B2B SaaS. Viết 3 tiêu đề email cho webinar về bảo mật dữ "
                  "liệu, nhắm tới quản lý IT. Mỗi tiêu đề dưới 45 ký tự, không emoji. "
                  "Đánh số 1-2-3.",
                  "1) Bảo mật SaaS: điều IT phải biết\n"
                  "2) Webinar bảo mật dữ liệu — bản IT\n"
                  "3) Dữ liệu của bạn, rủi ro của bạn")

    W = 880
    x0 = 44
    cw = W - 2 * x0
    fsize, lh = 19, 24

    def card(y, title, ptext, rtext, good, chip):
        pls = wrap(ptext, fsize, cw - 64)
        rls = wrap(rtext, 16, cw - 64)
        py = y + 92                      # first prompt-text baseline
        rlab = py + len(pls) * lh + 16   # "Model reply" label baseline
        ry = rlab + 20                   # first reply-text baseline
        h = ry + len(rls) * 21 + 20
        m = []
        m.append(rrect(x0, y, cw, h, 20, '#ffffff', '#fecaca' if not good else '#bbf7d0', 2))
        chip_w = 210 if lang == 'en' else 170
        m.append(rrect(x0 + 22, y + 16, chip_w, 34, 10, chip))
        m.append(center(title, x0 + 22 + chip_w / 2, y + 38, 18, '#ffffff', '700'))
        m.append(put_top(['Prompt'], x0 + 22, y + 72, 15, SUB, weight='700'))
        m.append(put_top(pls, x0 + 22, py, fsize, INK, lh=lh, weight='500'))
        m.append(put_top(['Model reply'], x0 + 22, rlab, 15, SUB, weight='700'))
        m.append(put_top(rls, x0 + 22, ry, 16, SUB, lh=21, weight='500'))
        return ''.join(m), h

    y = 36
    m1, h1 = card(y, weak[0], weak[1], weak[2], False, '#dc2626')
    y2 = y + h1 + 30
    m2, h2 = card(y2, strong[0], strong[1], strong[2], True, '#16a34a')
    H = y2 + h2
    return svg(W, H, m1 + m2)

jobs = {
    'llm-evals': [('eval-loop.svg', eval_loop), ('scorecard.svg', scorecard)],
    'rag-guide': [('rag-architecture.svg', rag_arch), ('open-book.svg', open_book)],
    'prompt-engineering': [('prompt-anatomy.svg', prompt_anatomy), ('before-after.svg', before_after)],
}

if __name__ == '__main__':
    base = '/Users/thienthuat/Desktop/evals-blog'
    for lang in ('en', 'vi'):
        for slug, fns in jobs.items():
            for fname, fn in fns:
                path = os.path.join(base, 'content', lang, slug, fname)
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(fn(lang))
                print('wrote', path)
