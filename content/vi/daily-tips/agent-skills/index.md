+++
date = '2026-09-09T09:00:00+07:00'
draft = false
pinned = true
title = 'Trang bị kỹ năng cho AI agent: SKILL.md là gì và khi nào nên dùng'
description = 'Prompt mô tả một câu trả lời; skill đóng gói một quy trình lặp lại được. Tìm hiểu quy ước SKILL.md để trao cho agent những "kỹ năng" tái sử dụng — cấu trúc, một ví dụ tối giản và khi nào nên dùng skill thay vì prompt hay RAG.'
summary = 'Prompt mô tả một câu trả lời; skill đóng gói một quy trình lặp lại được. Cấu trúc của một SKILL.md, ví dụ tối giản và khi nào nên dùng.'
featured_image = 'cover.svg'
show_reading_time = true
+++

Agent không chỉ trò chuyện: nó hành động — viết, ghi nhận, rà soát và sửa chữa qua nhiều bước. Làm tốt bất kỳ việc nào trong số đó cần một quy trình, chứ không chỉ sự thông minh. Dù mô hình có giỏi đến đâu, nó vẫn cần biết các bước của bạn, quy tắc của bạn, công cụ của bạn và định dạng đầu ra bạn muốn. Nếu quy trình đó ổn định và bạn chạy đi chạy lại, bạn không nên phải gõ lại nó mỗi lần. Đó là lúc agent skills xuất hiện: thứ bạn trao cho agent một lần để nó tự chạy mỗi khi cần.

![Agent skill cover](cover.svg)

*Bìa: skill là một quy trình lặp lại được mà agent tải về khi gặp đúng việc.*

## Skill của agent là gì

Agent skill — quy ước SKILL.md do Anthropic phổ biến và nay được nhiều framework agent hỗ trợ — là một thư mục đóng gói một năng lực lặp lại được. Trái tim của nó là một file markdown duy nhất, `SKILL.md`, hướng dẫn agent cách làm việc đó. Xung quanh nó, bạn có thể đặt bất cứ thứ gì quy trình cần: tài liệu tham khảo, script, template hay các bước kiểm tra.

Skill nằm im cho tới khi được cần. Agent thường chỉ thấy một danh sách skill kèm tên và mô tả ngắn; khi một việc khớp với mô tả, nó tải thư mục đó về và làm theo các bước. Không có gì bị nhồi vào system prompt, nên mỗi cuộc hội thoại bắt đầu gọn nhẹ, và đúng quy trình sẽ xuất hiện đúng lúc cần.

Hãy nghĩ skill như một cuốn runbook trao cho đồng nghiệp mới cẩn thận: prompt là *nói điều gì đó ngay bây giờ như thế nào*, còn skill là *làm việc gì đó, mỗi lần, như thế nào*.

## Cấu trúc của một SKILL.md

Một file skill tốt thì nhỏ gọn và tường minh. Các phần quan trọng:

- **Tên và mô tả** (front matter). Mô tả chính là “cò súng”: agent đọc nó để quyết định skill có hợp việc hay không. Hãy nói rõ skill làm gì *và khi nào dùng* — “Dùng khi người dùng nhờ dịch nội dung” hữu ích hơn nhiều so với “Dịch nội dung”.
- **Các bước được đánh số**. Quy trình theo thứ tự. Nếu bước hai phụ thuộc bước một, hãy nói rõ.
- **Quy tắc và giới hạn**. Nên làm gì, không bao giờ làm gì, và khi nào phải dừng lại hỏi thay vì đoán.
- **Hợp đồng đầu ra**. Định dạng, độ dài, giọng văn, ngôn ngữ và kết quả nên nằm ở đâu.
- **Các file hỗ trợ**. Mọi thứ các bước cần đến mà không nên nhét vào file hướng dẫn.

Một bố cục tối giản:

```text
skills/
└── translate-post/
    ├── SKILL.md
    └── tone-guide.md
```

Và một `SKILL.md` ngắn — ví dụ này dành cho việc dịch qua lại giữa tiếng Anh và tiếng Việt, đúng kiểu blog này đang viết:

```markdown
---
name: translate-post
description: Dịch một bài viết giữa tiếng Anh và tiếng Việt, giữ nguyên cấu
  trúc markdown và giọng văn. Dùng khi người dùng nhờ dịch nội dung
  hoặc nhắc tới bản EN/VI.
---

1. Đọc toàn bộ bài gốc trước khi viết bất cứ điều gì.
2. Giữ nguyên heading, danh sách, khối code, chú thích ảnh và đường liên kết.
3. Dịch tự nhiên cho người đọc mục tiêu; giữ các thuật ngữ như RAG, prompt
   và eval ở dạng tiếng Anh.
4. Không thêm thông tin mà bản gốc không có.
5. Trước khi kết thúc, đọc lại bản nháp một lượt để kiểm tra giọng văn
   và tính nhất quán.
```

Toàn bộ ý tưởng nằm ở đó: mô hình vốn đã biết viết; skill cho nó biết *quy trình của bạn*, và agent tự áp dụng mỗi khi cần.

## Agent chọn và chạy skill như thế nào

Hai chi tiết làm nên tính thực dụng của mô hình này:

- **Khám phá mà không tốn ngữ cảnh.** Agent đọc mô tả ngắn trước và chỉ tải cả skill khi thấy phù hợp. Đặt quy trình vào file thay vì vào system prompt giúp tiết kiệm ngữ cảnh và giữ cho prompt luôn ổn định.
- **Script lo phần chắc chắn.** Nếu một bước thuần logic — định dạng lại, tính toán, kiểm tra — skill có thể chạy một script nhỏ thay vì bắt mô hình tự suy luận mỗi lần. Mô hình ngôn ngữ giỏi phán đoán nhưng dở số học; đừng bắt chúng làm số học hai lần.

Skill có thể kết hợp: các bước của skill này có thể chuyển việc cho skill khác. Skill cũng version sạch sẽ trong git — điều quan trọng vì một skill gần với code hơn là văn xuôi.

## Skill, prompt hay RAG?

Ba công cụ chồng lấn nhau, và chọn đúng sẽ đỡ tốn công:

- **Prompt**: lựa chọn rẻ nhất cho việc một lần. Diễn đạt rõ ràng, một câu trả lời, không cần lưu trữ gì.
- **Skill**: dành cho *quy trình lặp lại được* — các bước ổn định, quy tắc rõ ràng và hợp đồng đầu ra. Nếu bạn đã dán cùng một khối hướng dẫn dài tới lần thứ ba, hãy đóng gói nó thành skill.
- **RAG**: dành cho *kiến thức thay đổi* — chính sách, tài liệu sản phẩm, ticket. Sự thật nên đến từ truy xuất, không nên nằm trong hướng dẫn. Hãy để skill mô tả *cách làm*; kiến thức nên nằm trong tài liệu mà skill có thể trỏ tới.

Skill không thay thế các biện pháp phòng vệ khác trong blog này. Một agent thực thi quy trình vẫn có thể hallucinate một bước hay bịa một nguồn, nên các thói quen vẫn còn nguyên: [kiểm tra những khẳng định quan trọng](/vi/daily-tips/why-ai-hallucinates-and-how-to-handle-it/), [gắn câu trả lời vào tài liệu](/vi/rag/rag-guide/) và [đo chất lượng bằng evals](/vi/evals/llm-evals/) — skill là code, và code xứng đáng có bộ kiểm thử.

## “Pave the cow path”

Cách bắt đầu tốt nhất không phải là thiết kế skill từ con số không. Hãy để ý một prompt bạn dùng đi dùng lại, trau chuốt tới khi nó chạy tốt, rồi ghi lại thành quy trình:

1. Viết các bước được đánh số đúng như bạn vẫn làm.
2. Thêm quy tắc tường minh và hợp đồng đầu ra.
3. Viết mô tả sao cho skill kích hoạt đúng lúc và im lặng khi không liên quan.
4. Thử trên ba việc thật; bổ sung những file còn thiếu.
5. Lưu vào git và rà soát thay đổi như với code.

## Những điểm chính

- Skill là một thư mục chứa `SKILL.md`: một quy trình lặp lại được mà agent tải về khi cần.
- Mô tả là “cò súng” — hãy ghi rõ skill làm gì *và khi nào dùng*.
- Đánh số các bước, nêu rõ quy tắc và chốt định dạng đầu ra.
- Prompt cho việc một lần, skill cho quy trình lặp lại, RAG cho kiến thức thay đổi.
- Skill là code: hãy version, rà soát và đo bằng evals.

**Đọc tiếp:** [cách đo chất lượng AI bằng LLM evals](/vi/evals/llm-evals/) và [prompt engineering](/vi/prompting/prompt-engineering/).
