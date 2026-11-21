---
title: 'Em test ứng dụng này kỹ chưa? Nhiều năm sau, tôi hiểu câu hỏi này là cả một sự nghiệp'
description: 'Thầy hỏi tôi có test kỹ ứng dụng chưa. Tôi đáp có. Nhiều năm sau tôi mới hiểu: trả lời câu hỏi ấy không phải việc của một buổi chiều — mà là công việc của cả một sự nghiệp.'
summary: 'Thầy hỏi tôi có test kỹ chưa, tôi đáp có. Thầy hỏi có test hết trường hợp chưa, tôi vẫn đáp có. Bảy năm sau tôi mới hiểu mình đã sai ở đâu.'
date: '2026-11-21T09:00:00+07:00'
draft: false
tags:
  - 'kiểm thử'
---

Trong buổi bảo vệ khoá luận tốt nghiệp năm 2019, một thầy trong hội đồng hỏi tôi một câu mà lúc đó tôi nghe như câu hỏi phụ:

"Em test ứng dụng này kỹ chưa?"

Tôi đáp không cần nghĩ: "Dạ kỹ rồi ạ. Em chạy hết các chức năng — thêm, sửa, xoá, tìm kiếm đều được."

Thầy không gật đầu. Thầy hỏi tiếp: "Em test được tất cả trường hợp chưa?"

Tôi vẫn đáp: "Dạ có ạ."

Giọng tôi lúc đó tự tin, trơn tru, và hoàn toàn không biết mình đang nói gì.

## Bảy năm sau

Nhân ngày 20/11, tôi nhớ lại buổi bảo vệ ấy — không phải vì câu trả lời sai, mà vì sự tự tin trong đó. Tôi đã trả lời "có" cho một câu mà người làm nghề đủ lâu không bao giờ trả lời "có": *Em test được tất cả trường hợp chưa?*

"Tất cả trường hợp" không phải một danh sách. Nó là một tập gần như vô hạn: mọi thứ người dùng có thể gõ, mọi thứ tự thao tác, mọi trạng thái mạng, mọi múi giờ, mọi lần hai người bấm cùng lúc. Không ai test hết được. Người giỏi không nói "em test hết"; họ nói: "Em đã test những chỗ này. Chỗ kia em chưa test. Đây là lý do em vẫn dám bàn giao."

Bảy năm trước tôi chưa phân biệt được hai câu đó. Bây giờ thì phân biệt được, và biết ơn thầy vì đã hỏi. Câu hỏi của thầy không phải để bắt bí. Nó là câu hỏi mà tôi sẽ phải tự hỏi mình mỗi lần bàn giao một thứ gì đó.

## Kiểm thử là một nghệ thuật

Nghệ thuật ở đây không phải chuyện thi vị hoá. Nó là ba quyết định khó, lặp đi lặp lại mỗi ngày:

- Chọn cái gì đáng test, khi thời gian không đủ cho tất cả.
- Viết ra kết quả đúng *trước khi* chạy, để không tự lừa mình bằng câu "thấy nó chạy mà".
- Đọc một test đỏ và hiểu nó đang nói gì — về code, về giả định, hay về chính yêu cầu.

Một phép thử chỉ là phép thử khi tôi biết trước kết quả đúng là gì. "Bấm vào nút, thấy màn hình chuyển" là quan sát, không phải kiểm thử. Kiểm thử cần ba thứ, viết ra trước khi chạy: một điều kiện xuất phát, một hành động, và một kết quả mong đợi.

Không có kết quả mong đợi, tôi chỉ có thể nói "nó vẫn chạy", chứ không thể nói "nó đúng". Và "vẫn chạy" là trạng thái của mọi ứng dụng chưa bị phát hiện lỗi — kể cả những ứng dụng đang làm mất dữ liệu của người dùng một cách rất im lặng.

## Một test case tử tế trông như thế nào

Một test case tốt đọc lên là hiểu, và người khác chạy lại được mà không cần hỏi tôi. Ví dụ với chức năng đăng ký tài khoản:

- Email mới, mật khẩu hợp lệ → tạo được tài khoản, đăng nhập được ngay.
- Email đã tồn tại → báo lỗi rõ ràng, và **không** tạo bản ghi thứ hai.
- Mật khẩu dưới 8 ký tự → bị chặn, kèm lý do cụ thể.
- Mất mạng giữa lúc gửi → không để lại tài khoản nửa vời.
- Bấm gửi hai lần liên tiếp → chỉ một tài khoản được tạo.

Chú ý điều thứ hai: kiểm tra rằng bản ghi **không** được tạo quan trọng ngang với kiểm tra nó được tạo. Phần lớn lỗi nghiêm trọng nằm ở vế này, và đó chính là phần mà một buổi chiều "bấm thử cho vui" hay bỏ qua.

## Test theo rủi ro, không theo số lượng

Không test đều mọi thứ — thời gian không cho phép, và cũng không cần. Tôi hỏi: nếu chỗ này hỏng, thiệt hại là gì? Thanh toán sai một đồng, mất dữ liệu, lộ thông tin riêng tư, hay chỉ là một chữ bị lệch? Câu trả lời quyết định tôi dồn công sức vào đâu.

Con số coverage hữu ích để phát hiện vùng code chưa ai chạm tới, nhưng nó không nói được là tôi đã test đúng chỗ quan trọng hay chưa. 80% coverage dồn hết vào phần trang trí là 80% vô nghĩa.

## Lỗi sống ở biên

Lỗi hiếm khi nằm ở giữa miền giá trị. Nó nằm ở mép:

- danh sách rỗng, danh sách một phần tử, danh sách rất dài;
- chuỗi rỗng, chuỗi 10.000 ký tự, emoji, tiếng Việt có dấu, ký tự `<` và `&`;
- số 0, số âm, số rất lớn, số thập phân;
- hai người sửa cùng một bản ghi cùng lúc;
- múi giờ, giờ mùa hè, và thời điểm đúng nửa đêm.

Nếu tôi chưa thử những trường hợp này, tôi chưa biết ứng dụng của mình làm gì. Tôi chỉ biết nó làm gì trong điều kiện thuận lợi nhất — tức là điều kiện mà người dùng thật hiếm khi gặp.

## Ba tầng, và câu hỏi của mỗi tầng

Không phải mọi thứ cần test ở cùng một mức:

- **Unit** — logic thuần có đúng không? Nhanh, rẻ, chạy hàng nghìn cái trong vài giây. Viết nhiều ở đây.
- **Integration** — các mảnh ghép với thế giới thật có khớp không? Cơ sở dữ liệu, API bên ngoài, hàng đợi, quyền, thời gian. Đây là nơi dễ vỡ nhất.
- **End-to-end** — người dùng thật đi hết một luồng có thành công không? Đắt, chậm, hay "flaky", nên chỉ dùng cho vài luồng sống còn.

Sai lầm phổ biến của người mới — và của tôi tám năm trước — là chỉ có một trong hai: hoặc vài unit test cho đẹp con số, hoặc bấm tay từ đầu đến cuối rồi gọi đó là kiểm thử.

## Thời AI agent: code rẻ đi, kiểm chứng đắt hơn

Bảy năm trước tôi viết từng dòng code bằng tay, nên tôi tin vào code vì tôi đã viết nó. Bây giờ một phần code do AI viết, trong vài giây, và tôi không còn lý do nào để tin nó chỉ vì nó tồn tại.

Agent có thể tự sinh test, tự chạy, tự sửa khi test đỏ. Nhưng nó không biết "đúng" nghĩa là gì thay tôi. Nếu tôi không nói được điều gì là đúng, agent sẽ viết ra một bài test chỉ kiểm tra đúng cái nó vừa làm — và cả hai cùng đồng ý rằng mọi thứ đều ổn.

Khi tốc độ viết code tăng lên, phần kiểm chứng trở thành thứ quyết định chất lượng. Câu hỏi của thầy vì thế không cũ đi — nó khó trả lời hơn, vì số trường hợp tăng nhanh hơn số test tôi kịp viết. Và vì thế, thời AI agent lại là thời kiểm thử quan trọng hơn cả.

## Danh sách tôi tự trả lời trước khi bàn giao

Trước khi nộp, trước khi demo, trước khi nói "xong rồi", tôi tự trả lời:

- Mỗi yêu cầu có ít nhất một test case, và kết quả mong đợi được viết ra chứ không nằm trong đầu.
- Đã thử dữ liệu sai, dữ liệu rỗng, và dữ liệu quá lớn.
- Đã thử hai hành động cùng lúc, và thử bấm lại.
- Thông báo lỗi nói người dùng cần làm gì, không lộ stack trace.
- Test chạy được trên máy người khác, không chỉ trên máy tôi.
- Tôi biết rõ chỗ nào chưa test, và vì sao chấp nhận được.

## Lời đáp cho thầy

Nếu có dịp gặp lại thầy, tôi sẽ không trả lời "dạ có" nữa.

Tôi sẽ nói: "Em đã test những chỗ này. Em chưa test những chỗ kia. Rủi ro còn lại là như thế này, và em dám bàn giao vì em biết nó là gì."

Đó là câu trả lời của một người làm nghề, không phải của một cậu sinh viên sợ bị hỏi khó. Bảy năm mới trả lời được, nhưng dù sao vẫn còn kịp — và tôi vẫn nhớ câu hỏi của thầy mỗi lần bấm nút bàn giao.
