---
date: '2026-09-14T09:00:00+07:00'
draft: true
pinned: true
title: 'AI agents là gì? Phân biệt LLM và AI Agents'
description: 'LLM trả lời một câu hỏi; AI agent theo đuổi một mục tiêu qua nhiều bước. Tìm hiểu agent là gì, vòng lặp bên trong nó, và khi nào nên dùng LLM, khi nào nên dùng agent.'
summary: 'LLM nhận câu hỏi rồi trả lời; AI agent nhận mục tiêu, gọi công cụ và tự lặp cho tới khi xong. Phân biệt rõ hai thứ — và khi nào nên dùng cái nào.'
featuredImage: '/images/posts/vi/daily-tips/what-are-ai-agents/cover.svg'
---

Bạn mở một chatbot, gõ câu hỏi và nhận câu trả lời. Đó là một LLM. Rồi bạn giao hẳn một việc: “tìm lỗi trong bản dịch này, sửa, chạy lại kiểm tra và mở pull request”. Lần này nó không chỉ trả lời — nó đọc file, sửa, chạy lệnh, đọc lỗi, sửa tiếp và báo cáo khi xong. Đó là một AI agent.

Hai thứ này thường bị gọi lẫn nhau, nhưng khác nhau ở một điểm cốt lõi: **LLM tạo ra văn bản; agent theo đuổi một mục tiêu.** Bài này tách rõ từng cái, mô tả vòng lặp bên trong một agent, và khi nào bạn thực sự cần đến nó.

![AI agents cover](/images/posts/vi/daily-tips/what-are-ai-agents/cover.svg)

*Bìa: agent = một LLM + công cụ + một vòng lặp.*

## LLM là gì?

LLM (large language model) là một mô hình được học từ lượng lớn văn bản để dự đoán token tiếp theo. Bạn đưa văn bản vào, nó trả văn bản ra. Mỗi lần gọi như vậy là một lượt độc lập.

Ba tính chất quan trọng:

- **Một lượt**: nhận prompt, trả lời, hết. Muốn nó làm tiếp thì bạn phải hỏi tiếp.
- **Không tự hành động**: nó không mở file, không gọi API, không bấm nút. Nó chỉ nói.
- **Không nhớ mặc định**: API không tự lưu hội thoại; “trí nhớ” bạn thấy trong các app chat thực ra là ứng dụng gửi lại lịch sử mỗi lần.

Và vì bản chất là dự đoán, LLM có thể tạo ra câu trả lời nghe rất hợp lý nhưng sai — đó là [hallucination](/vi/daily-tips/why-ai-hallucinates-and-how-to-handle-it/). Mô hình không kiểm tra sự thật; nó chọn chuỗi từ có xác suất cao nhất.

## AI agent là gì?

AI agent là một hệ thống lấy LLM làm bộ não, rồi thêm ba thứ để nó có thể *hành động*:

- **Công cụ (tools)**: tìm kiếm web, đọc và ghi file, chạy code, gọi API, truy vấn cơ sở dữ liệu.
- **Trạng thái và bộ nhớ (state)**: những gì agent đã biết và đã làm — kế hoạch, kết quả từng bước, file đã sửa.
- **Vòng lặp điều khiển (control loop)**: phần quyết định bước tiếp theo, chạy công cụ, đọc kết quả rồi lặp lại cho tới khi xong hoặc bị dừng.

Nói cách khác: **agent = model + harness**. Model vẫn là LLM bạn đã biết; cái mới là phần khung cho nó quan sát môi trường và thay đổi môi trường.

## Vòng lặp của một agent

Hầu hết agent đều xoay quanh một vòng lặp đơn giản:

![Agent loop](/images/posts/vi/daily-tips/what-are-ai-agents/agent-loop.svg)

*Agent lặp cho tới khi đạt mục tiêu — hoặc tới khi bị con người dừng lại.*

Ví dụ với việc “sửa lỗi build”:

1. **Mục tiêu**: người dùng giao “build đang đỏ, sửa cho xanh”.
2. **Lập kế hoạch**: đọc log, tìm file liên quan, đoán nguyên nhân.
3. **Hành động**: chạy lệnh, mở file, sửa một dòng.
4. **Quan sát**: chạy lại build, đọc lỗi mới.
5. **Lặp lại**: nếu còn lỗi thì quay lại bước 2; nếu đã xanh thì báo cáo.

Điểm cốt lõi: đường đi không được viết sẵn. Chính mô hình quyết định bước tiếp theo dựa trên kết quả vừa quan sát.

## Phân biệt LLM và AI agent

![LLM vs AI agent](/images/posts/vi/daily-tips/what-are-ai-agents/llm-vs-agent.svg)

*Cùng một mô hình, nhưng một bên chỉ trả lời còn một bên hành động và tự lặp.*

| Tiêu chí | LLM | AI agent |
| --- | --- | --- |
| Đầu vào | Câu hỏi, prompt | Mục tiêu |
| Đầu ra | Văn bản | Hành động và kết quả |
| Số bước | Một lượt | Nhiều bước, lặp lại |
| Công cụ | Không | Có (file, shell, API…) |
| Trạng thái | Quên giữa các lượt | Giữ qua nhiều bước |
| Vai trò của bạn | Hỏi từng bước | Giao việc rồi giám sát |
| Rủi ro chính | Nói sai | Nói sai *và* làm sai |
| Cách đo | Chấm câu trả lời | Chấm câu trả lời + kiểm thử quy trình |

Hàng cuối là hàng quan trọng nhất. Khi LLM chỉ nói, một lỗi tốn vài phút đọc lại. Khi agent hành động, cùng lỗi đó có thể xoá nhầm file, gửi nhầm email hoặc tiêu tiền thật.

## Ranh giới không rõ ràng — và điều đó bình thường

“LLM hay agent” không phải hai chiếc hộp tách biệt mà là một phổ tự chủ:

- Một chatbot chỉ trả lời là LLM thuần.
- Thêm tìm kiếm web hoặc đọc tài liệu (như [RAG](/vi/rag/rag-guide/)) là đã có một phần hành động.
- Cho nó tự quyết định gọi công cụ nào, theo thứ tự nào, trong bao nhiêu bước — đó mới là agent đúng nghĩa.

Ở giữa có một mức rất hữu ích: **workflow**. Bạn viết sẵn các bước cố định (ví dụ: trích văn bản → tóm tắt → dịch → kiểm tra định dạng), mỗi bước do một lời gọi model đảm nhiệm. Workflow rẻ hơn, ổn định hơn và dễ gỡ lỗi hơn agent tự do. Nếu đường đi đã biết trước, hãy dùng workflow; chỉ chuyển sang agent khi cần model tự quyết định bước tiếp theo.

## Khi nào dùng cái nào?

- **LLM một lượt**: viết, tóm tắt, phân loại, trả lời câu hỏi, gợi ý. Nhanh, rẻ, dễ đoán.
- **Workflow**: quy trình nhiều bước nhưng cố định, bạn biết rõ thứ tự.
- **Agent**: việc mở, cần công cụ, đường đi phụ thuộc vào kết quả từng bước — sửa lỗi, nghiên cứu, điều tra dữ liệu, vận hành.

Một cách kiểm tra nhanh: nếu bạn có thể viết quy trình thành các bước cố định thì bạn chưa cần agent. Nếu bạn thấy mình phải mô tả *cách phản ứng với mọi tình huống có thể xảy ra*, đó là dấu hiệu nên để agent tự quyết.

## Một số AI agent đang được dùng trên thị trường

Danh sách dưới đây chỉ để bạn có điểm neo, không phải một bảng xếp hạng — thị trường này đổi theo từng tháng.

**Agent lập trình**

- **Claude Code** (Anthropic) — agent chạy trong terminal: đọc repo, sửa file, chạy test rồi tự kiểm tra lại.
- **OpenAI Codex** — agent lập trình chạy được cả trên cloud lẫn local, hợp với những việc dài hơi.
- **Cursor (Agent Mode)** — agent nằm ngay trong IDE, sửa nhiều file một lúc.
- **GitHub Copilot (coding agent)** — agent gắn với pull request và quy trình trên GitHub.
- **Devin** (Cognition) — hướng tới tự chủ hoàn toàn: nhận việc rồi trả về kết quả để bạn duyệt.
- **Cline** và **Aider** — mã nguồn mở, bạn tự mang API key.

**Agent dùng chung và điều khiển máy tính**

- **ChatGPT Agent / Operator** (OpenAI) — tự duyệt web, điền form và làm việc nhiều bước.
- **Claude với computer use** (Anthropic) — mô hình điều khiển chuột, bàn phím và trình duyệt.
- **Gemini agents** (Google) — agent nằm trong hệ sinh thái Google.
- **Microsoft Copilot agents** — agent trong Teams, Outlook và SharePoint.

**Agent nghiên cứu, duyệt web**

- **OpenAI Deep Research** và **Gemini Deep Research** — tự tìm, đọc nhiều nguồn rồi tổng hợp thành báo cáo.
- **Perplexity** — tìm kiếm kèm trích nguồn theo kiểu agent.
- **Browser Use** — thư viện mã nguồn mở để tự dựng agent duyệt web.

**Agent cho doanh nghiệp**

- **Salesforce Agentforce** và **ServiceNow AI Agents** — agent gắn với quy trình nội bộ.
- **Sierra** và **Intercom Fin** — agent chăm sóc khách hàng.
- **Microsoft Copilot Studio** và **Amazon Bedrock Agents** — nền tảng để đội của bạn tự dựng agent.

**Khung để tự dựng agent** — không phải sản phẩm bán sẵn nhưng đáng biết: **LangGraph** (LangChain), **CrewAI**, **Microsoft AutoGen**, **OpenAI Agents SDK**.

Điều đáng chú ý: gần như mọi hãng lớn đều đang gọi sản phẩm của mình là “agent”. Vì vậy khi đánh giá, đừng hỏi “cái này có phải agent không”, mà hỏi agent đó **được phép làm gì, tự quyết bao nhiêu bước, và ai dừng nó lại** — đúng ba thứ vừa bàn ở trên.

## Agent cũng sai — và sai thì đắt hơn

Agent thừa hưởng mọi điểm yếu của LLM, rồi nhân lên vì nó có quyền hành động:

- Hallucination biến thành **hành động sai**: xoá nhầm file, sửa nhầm chỗ, gọi sai API.
- Lỗi nhỏ có thể **cộng dồn** qua nhiều bước.
- Agent có thể **lặp vô hạn** hoặc đi lạc khỏi mục tiêu ban đầu.

Vì vậy, vài nguyên tắc thực tế:

- **Quyền tối thiểu**: chỉ cấp những công cụ và quyền mà việc đó thực sự cần.
- **Chạy trong môi trường cô lập**: sandbox, nhánh git riêng, môi trường staging.
- **Chốt chặn cho việc nguy hiểm**: xoá dữ liệu, gửi ra ngoài, chi tiền — cần con người duyệt.
- **Ghi log mọi bước**: bạn cần biết nó đã gọi gì và nhận lại gì.
- **Đo bằng evals**: không chỉ chấm câu trả lời cuối mà kiểm thử cả quy trình — xem [LLM evals](/vi/evals/llm-evals/).

Và nếu bạn thấy mình giao lặp đi lặp lại cùng một quy trình cho agent, hãy đóng gói nó thành [agent skill](/vi/daily-tips/agent-skills/) để chạy ổn định và version như code.

## Điểm chính

- **LLM tạo văn bản; agent theo đuổi mục tiêu.** Cùng một mô hình, khác ở chỗ có hành động và vòng lặp hay không.
- Agent = **model + công cụ + trạng thái + vòng lặp điều khiển**.
- Vòng lặp cơ bản: mục tiêu → lập kế hoạch → hành động → quan sát → lặp lại.
- Nếu đường đi cố định, hãy dùng **workflow** thay vì agent tự do — rẻ hơn và dễ gỡ lỗi hơn.
- Tự chủ đi kèm rủi ro: cấp quyền tối thiểu, chạy trong sandbox, chốt chặn việc nguy hiểm và đo bằng evals.
- Có rất nhiều sản phẩm đang gắn nhãn “agent”: hãy đánh giá theo quyền hạn và mức tự chủ, đừng theo tên.

**Đọc tiếp:** [trang bị kỹ năng cho AI agent](/vi/daily-tips/agent-skills/), [đo chất lượng bằng LLM evals](/vi/evals/llm-evals/) và [RAG thực hành](/vi/rag/rag-guide/).
