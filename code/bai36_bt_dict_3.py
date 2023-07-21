#Cho data 1 cửa hàng, dữ liệu kiểu như sau :
#1. Tìm tất cả user có số điện thoại kết thúc bằng 8
#2: tìm tất cả user o có địa chỉ email
d=[{"name":"Tuan","phone":"555-1414","email":"galailaptrinh@gmail.com"},
    {"name":"Hung","phone":"555-1618","email":"galaixapxinh@gmail.com"},
    {"name":"Trung","phone":"555-3141","email":""},
    {"name":"Hoang","phone":"555-2718","email":"loli@gmail.com"},
]
print("cac user co so dien thoai ket thuc taij 8")
for dong in d:
    phone_check= dong["phone"]
    if phone_check[-1]== "8":
        phone_show= dong["phone"]
        name_show= dong["name"]
        email_show= dong["email"]
        print("+_____"*10)
        print(phone_show)
        print(name_show)
        print(email_show)
print("cac user khong co email: ")
for dong in d:
    email_check= dong["email"]
    if email_check=="":
        name_show2 = dong["name"]
        phone_show2 = dong["phone"]
        print(name_show2)
        print(phone_show2)

