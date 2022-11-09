#Thuat toan
<br>
B1: save frame_image cách nhau 0.5 giây mỗi video lưu vào mỗi video một thư mục ảnh
<br>
B2: Tìm pretrain model về face an-ti spoofing
<br>
B3: Lấy pretrain model inference lại toàn bộ ảnh trên. Lấy kết quả lưu vào hai thư mục : liveness và spoof
<br>
B4: Nếu nhiều việc thì bỏ bước 3
<br>
B5: Lấy model inference tất các các video: Mỗi video lấy 30 frame ngẫu nhiên
<br>
Nếu số ảnh frame liveness > số ảnh spoof thì video đó là liveness. Còn không là ngược lại
<br>
B6: Save kết quả video(vd :video:0 (0 là liveness) video:1(1 là spoof)) vào file csv
