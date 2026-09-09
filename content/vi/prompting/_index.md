+++
title = 'Prompt engineering'
description = 'Cùng một mô hình nhưng câu trả lời rất khác nhau tùy cách bạn hỏi. Tìm hiểu cấu trúc của một prompt tốt, kỹ thuật hiệu quả, và khi nào viết prompt thôi là chưa đủ.'
[menu.main]
  name = 'Prompt engineering'
  weight = 30
  url = '/vi/prompting/'
+++

# Prompt engineering

Cách diễn đạt chính là cách điều khiển: mô hình ngôn ngữ trả lời theo hình dáng của yêu cầu, nên prompt mơ hồ dễ nhận câu trả lời mơ hồ, còn prompt rõ ràng thì kéo câu trả lời sát với ý bạn hơn. Prompt engineering là cách rẻ nhất để tận dụng mô hình bạn đang có — không cần huấn luyện lại, không cần công cụ mới, chỉ cần chỉ dẫn rõ ràng hơn.

Các bài trong chủ đề này nói về cấu trúc của một prompt tốt (vai trò, bối cảnh, nhiệm vụ, định dạng, ví dụ), kỹ thuật nào tạo khác biệt lớn nhất và cách “debug” prompt như debug code.

## Chủ đề này nằm ở đâu

Prompt không thể thêm kiến thức mà mô hình chưa từng có — đó là việc của [RAG](/vi/rag/) — và cũng không cho bạn biết câu trả lời có thực sự tốt hay không, điều mà [LLM evals](/vi/evals/) đo lường. Bên dưới cả hai là failure mode [hallucination](/vi/daily-tips/why-ai-hallucinates-and-how-to-handle-it/) mà các chủ đề này cùng xử lý.
