#1 Để cho 1 website hoạt động bình thường, cần bao nhiều machines hoạt động?

# 2 máy hoạt động:
# + Server: Chứa tất cả mọi thứ (gồm Code chạy, Data)
# + Client: Máy của người dùng


#2 Profile cá nhân có bị mất khi log out không?
Không, vì được lưu tại Server


# 3 Sub-pages trong genk.vn

Hình thức đã có hết (Template Rendering), dữ liệu chỉ cần đẩy lên


# 4 Remember me của facebook để login thì không cần đăng nhập trong bao nhiêu ngày?

2 tháng

User & pass được coi  như một token ngay sau khi truy cập.

# 5: Quy trình Enter website  => Nội dung buổi hôm nay

Client -> gửi Request -> Server (người phục vụ)

Nếu Client chỉ muốn để xem, không thay đổi: gọi là GET

Server gửi trả lại file HTML & CSS  

Client chính là Chrome, Firefox

(Server đặt trong phòng lạnh)

Framework: Là bộ thư viện

=> Back-end: Chỉ lo về tính logic bên trong, không quan tâm đến bố cục
-> Front-end: Phụ trách về thẩm mỹ