#bài tập: nhập vào chuỗi bất kỳ
# sau đó chuyển thành chuỗi mã hoá vơí cách thức đã
# định dạng từ trước
message = input("Enter your message: ").lower() # nhập vào tin nhắn và chuyển về chữ thường
a = "abcdefghijklmnopqrstuvwxyz"
b = "zxcvbnmasdfghjklqwertyuiop"

encrypted_message = "" # khởi tạo chuỗi mã hóa

for char in message:
    if char in a:
        encrypted_message += b[a.index(char)]
    else:
        encrypted_message += char

print("Encrypted message: ", encrypted_message)
