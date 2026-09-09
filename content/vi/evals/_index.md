+++
title = 'LLM evals'
description = 'Cách đo chất lượng AI: xây một bộ eval nhỏ, chấm điểm cùng một cách sau mỗi thay đổi và phát hiện chất lượng đi xuống trước khi người dùng gặp phải.'
[menu.main]
  name = 'LLM evals'
  weight = 40
  url = '/vi/evals/'
+++

# LLM evals

Demo thì rất thích nhưng chẳng đo được gì: ở môi trường thật, người dùng hỏi những câu bạn không chọn trước, và mô hình cũng “trôi” giữa các phiên bản. Evals giải quyết việc đó — một bộ tình huống tiêu biểu nhỏ, được chấm điểm cùng một cách ở mỗi lần chạy, và chạy lại mỗi khi bạn đổi prompt hay đổi mô hình. Cảm xúc trở thành con số so sánh được.

Các bài trong chủ đề này hướng dẫn đo cái gì, bắt đầu nhỏ thế nào, các cách chấm điểm đơn giản và chạy evals như một vòng lặp chống regression.

## Chủ đề này nằm ở đâu

Evals là bước cuối của vòng lặp thực hành mà blog theo đuổi: hiểu vì sao mô hình [hallucinate](/vi/daily-tips/why-ai-hallucinates-and-how-to-handle-it/), [gắn câu trả lời vào tài liệu](/vi/rag/) và [ra lệnh rõ ràng](/vi/prompting/) — rồi mới kiểm tra chất lượng có thực sự được giữ vững hay không.
