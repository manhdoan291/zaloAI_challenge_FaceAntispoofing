#Thuat toan
<br>
B1: save frame_image cách nhau 0.5 giây mỗi một video sẽ có 1 thư mục ảnh chứa các frame
<br>
B2: Tìm pretrain model về face an-ti spoofing classification
<br>
B3: Lấy pretrain model inference lại toàn bộ ảnh trên. Lấy kết quả lưu vào hai thư mục : liveness và spoof
<br>
B4: Nếu nhiều việc thì bỏ bước 3
<br>
B5: Mỗi video lấy 30 frame ngẫu nhiên. Lấy model sẽ inference ra kết quả tất các các image trong tất cả các video 
<br>
Nếu số ảnh frame ngẫu nhiên liveness > số ảnh spoof thì video đó là liveness. Còn không là ngược lại
<br>
B6: Save kết quả video(vd :video:0 (0 là liveness) video:1(1 là spoof)) vào file csv
