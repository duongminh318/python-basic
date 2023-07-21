# 1. tính tổng các số trong chuỗi trên
# 2. tính trung bình cộng

'''
str1="English = 78 Science = 83 Math= 68 History= 65"
element = str1.split()
print(element)
sum=0
count =0
for i in element:
    if i.isnumeric():
        sum+=int(i)
        count+=1
arg= sum/count
print(count)
print("tong cac so cua chuoi: ", sum)
print("trung binh cac so: ", arg)'''

#bai tap 2
# viết chương trình kiểm tra tính hợp lệ của mật khẩu
# aaaaaAAAAA1
# mật khẩu hợp lệ khi có ít nhất 6 ký tự chứa 1 chữ cái
# (chữ thường hoặc hoa đều được)
# chứa ít nhất 1 chữ số
# 2. cho người dùng nhập vào mật khẩu đ login/ so sánh, nếu đúng mở cửa, sai quá 5 lần
# khoa dang nhập, thoát chương trình


'''import re
# Hàm kiểm tra tính hợp lệ của mật khẩu
def is_valid_password(password):
    # Kiểm tra chiều dài mật khẩu
    if len(password) < 6:
        return False
    # Kiểm tra chứa ít nhất 1 chữ cái
    if not re.search('[a-zA-Z]', password):
        return False
    # Kiểm tra chứa ít nhất 1 chữ số
    if not re.search('[0-9]', password):
        return False
    return True
# Biến đếm số lần nhập sai mật khẩu
count = 0
# Vòng lặp yêu cầu người dùng nhập mật khẩu
while True:
    password = input("Nhập mật khẩu của bạn: ")
    if is_valid_password(password):
        print("Mật khẩu hợp lệ. Chúc mừng, bạn đã đăng nhập thành công!")
        break
    else:
        count += 1
        print("Mật khẩu không hợp lệ. Vui lòng nhập lại.")
        if count >= 5:
            print("Bạn đã nhập sai quá nhiều lần. Tài khoản của bạn đã bị khóa.")
            break
'''
#cách khác ko sử dung re

'''# Nhập mật khẩu
password = input("Nhập mật khẩu: ")
# Tạo biến đếm số lượng ký tự chữ cái và số trong mật khẩu
num_letters = 0
num_digits = 0

# Kiểm tra mật khẩu có ít nhất 6 ký tự
if len(password) >= 6:
    # Duyệt từng ký tự trong mật khẩu
    for char in password:
        # Kiểm tra ký tự là chữ cái hoặc số
        if char.isalpha():
            num_letters += 1
        elif char.isdigit():
            num_digits += 1
    # Kiểm tra mật khẩu có ít nhất 1 chữ cái và 1 số
    if num_letters >= 1 and num_digits >= 1:
        print("Mật khẩu hợp lệ!")
    else:
        print("Mật khẩu không hợp lệ: phải có ít nhất 1 chữ cái và 1 số.")
else:
    print("Mật khẩu không hợp lệ: phải có ít nhất 6 ký tự.")


# yêu cầu người dùng nhập mật khẩu
password = input("Nhập mật khẩu để đăng nhập: ")

# đặt biến số lần nhập sai ban đầu bằng 0
wrong_attempts = 0

# kiểm tra tính hợp lệ của mật khẩu và cho phép đăng nhập
while True:
    # kiểm tra tính hợp lệ của mật khẩu
    if len(password) < 6 or not any(c.isalpha() for c in password) or not any(c.isdigit() for c in password):
        print("Mật khẩu không hợp lệ. Vui lòng nhập lại.")
        wrong_attempts += 1
        if wrong_attempts > 5:
            print("Bạn đã nhập sai mật khẩu quá nhiều lần. Tài khoản của bạn đã bị khóa.")
            break
        password = input("Nhập mật khẩu để đăng nhập: ")
    # đăng nhập nếu mật khẩu hợp lệ
    else:
        print("Đăng nhập thành công!")
        break
'''
x=bool
y=bool



#print(x,y)
n=input("Mời bạn tạo mật khẩu(ít nhất 6 kí tự và chứa ít nhất 1 chữ cái thường,1 chữ viết Hoa, 1 số): " )
while True:
    for i in n:
        if i.isdigit():
            x = True
            break
        else:
            x = False
    for i in n:
        if i.isalpha():
            y = True
            break
        else:
            y = False
    if len(n)<6 or x==False or y==False:
        n=input("Nhập lại MK, ít nhất 6 ký tự, ít nhất 1 chữ cái và 1 số")
    else:
        print("Mật khẩu hợp lệ")
        break



#2: y so 2
s = input("Mời nhập mật khẩu đăng nhập hệ thống : ")
dem=0
while s!=n:
    dem=dem+1
    s = input(f"Nhập lại mật khẩu( bạn đã nhập sai {dem}/5 lần)  : ")
    if dem==4:
        print("Bạn nhập sai quá 5 lần, khóa đăng nhập")
        break
else:
    print("Đăng nhập hệ thống thành công")