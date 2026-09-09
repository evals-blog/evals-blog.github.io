+++
title = 'RAG'
description = 'Mô hình chỉ biết dữ liệu huấn luyện của nó. RAG cho AI đọc tài liệu của bạn trước khi trả lời — gắn câu trả lời vào sự thật, giảm hallucination và giúp AI dùng được cho thông tin mới hoặc riêng tư.'
[menu.main]
  name = 'RAG'
  weight = 20
  url = '/vi/rag/'
+++

# RAG

Kiến thức của một mô hình chỉ là “ảnh chụp” văn bản công khai tại một thời điểm. Quy định, tài liệu sản phẩm, ticket hỗ trợ của bạn chưa từng nằm trong đó — nên khi được hỏi về chúng, mô hình trả lời theo mẫu chứ không theo sự thật. Retrieval-Augmented Generation (RAG) lấp khoảng trống đó: trước tiên tìm trong tài liệu của bạn, đưa các đoạn liên quan vào prompt, rồi để mô hình viết dựa trên những gì nó vừa đọc.

Các bài trong chủ đề này trình bày pipeline (ingest, retrieve, generate), một đoạn code tối giản và những nút tinh chỉnh quan trọng.

## Chủ đề này nằm ở đâu

RAG là câu trả lời chính cho vấn đề [hallucination](/vi/daily-tips/why-ai-hallucinates-and-how-to-handle-it/) mà bài đầu của blog đã nêu. Kết hợp RAG với [prompt rõ ràng](/vi/prompting/) để mô hình làm đúng chỉ dẫn, và giữ một vòng [LLM evals](/vi/evals/) để chất lượng không lặng lẽ tụt xuống.
