# Kiro Password Manager

[← Danh sách ứng dụng](../README.md)

Kiro Password Manager lưu mật khẩu và thông tin tài khoản trong kho mã hóa trên thiết bị. Tạo kho bằng mật khẩu chính, tổ chức dữ liệu theo thư mục và thẻ, rồi tìm kiếm, xem hoặc sửa tài khoản trong một giao diện thống nhất.

Kho được lưu thành file `.akpr` mã hóa. Ứng dụng không yêu cầu tài khoản trực tuyến; mạng được dùng để kiểm tra bản cập nhật và tải icon, favicon theo lựa chọn của người dùng.

## Tính năng

- Quản lý mật khẩu, ghi chú, thông tin API, biến môi trường và các trường tùy chỉnh.
- Tổ chức theo thư mục, thẻ, mục yêu thích; bấm badge thẻ ở sidebar để lọc tài khoản.
- Tạo mật khẩu, xem mã TOTP và hiển thị một phần mật khẩu với vị trí che thay đổi sau mỗi lần bấm.
- Chọn logo thương hiệu, ngân hàng, ảnh từ URL hoặc favicon của website. Ảnh được lưu trong kho mã hóa và giữ lại đến khi người dùng đổi ảnh hoặc icon.
- Xem thời gian cập nhật gần nhất ở bên phải từng dòng tài khoản.
- Xem lịch sử sửa đổi, sao lưu tự động hoặc thủ công, khôi phục và xuất kho mã hóa.
- Nhập dữ liệu KeePass `.kdbx` với bước xem trước trước khi tạo kho mới.
- Tự khóa kho, kiểm soát thời gian hiển thị mật khẩu và xóa clipboard do ứng dụng quản lý.

## Tải và cài đặt

| Thông tin | Bản hiện tại |
| --- | --- |
| Phiên bản | **1.0.17** |
| Hệ điều hành | macOS 13 trở lên |
| Kiến trúc | Apple Silicon (arm64) |
| Trạng thái | Bản thử nghiệm, ký ad hoc, chưa notarize |

**[Tải Kiro Password Manager 1.0.17 cho macOS (.app.tar.gz)](https://github.com/ngankt2/appkiro.com/releases/download/appkiro-password-manager-v1.0.17/KiroPasswordManager_1.0.17_arm64.app.tar.gz)**

1. Giải nén file tải về để nhận `Kiro Password Manager.app`.
2. Chuyển ứng dụng vào Applications.
3. Thoát bản cũ nếu đang chạy, rồi mở bản mới.

## Cập nhật 1.0.17

- Sử dụng tên sản phẩm **Kiro Password Manager** trên giao diện.
- Bổ sung bộ lọc thẻ ở sidebar và lưu ảnh icon, favicon để dùng lại.
- Mở rộng logo thương hiệu với WeChat, Messenger và các ngân hàng quốc tế; điều chỉnh hộp chọn để nhãn dễ đọc trên cửa sổ nhỏ.
- Đặt thời gian cập nhật bên phải từng tài khoản: `HH:mm` nếu cùng ngày, `dd/MM` nếu cùng năm và `dd/MM/yyyy` nếu khác năm.
- Thay đổi ngẫu nhiên các vị trí bị che khi xem một phần mật khẩu.

Có thể kiểm tra bản mới từ Cài đặt, menu ứng dụng hoặc số phiên bản ở chân trang. Ứng dụng cũng kiểm tra khi khởi động và mỗi sáu giờ khi đang hiển thị. Người dùng chủ động chọn tải, cài đặt và khởi động lại.

| Tài nguyên cập nhật | Liên kết |
| --- | --- |
| Bản phát hành hiện tại | [Kiro Password Manager 1.0.17](https://github.com/ngankt2/appkiro.com/releases/tag/appkiro-password-manager-v1.0.17) |
| Chữ ký gói cập nhật | [.sig](https://github.com/ngankt2/appkiro.com/releases/download/appkiro-password-manager-v1.0.17/KiroPasswordManager_1.0.17_arm64.app.tar.gz.sig) |
| Mã kiểm tra SHA-256 | [SHA256SUMS](https://github.com/ngankt2/appkiro.com/releases/download/appkiro-password-manager-v1.0.17/SHA256SUMS) |
| Kênh cập nhật | [latest.json](https://raw.githubusercontent.com/ngankt2/appkiro.com/main/updates/appkiro-password-manager/latest.json) |
| Lịch sử phiên bản | [Các bản phát hành Kiro Password Manager](https://github.com/ngankt2/appkiro.com/releases?q=appkiro-password-manager) |
