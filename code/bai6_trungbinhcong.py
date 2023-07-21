'''nhập từ bàn phím thời gian chạy của 3 vận động viên và tính trung bình cộng thời gian đó'''
print("mời nhập vào thời gian về đích của ba vận động viên")
a = float(input("thời gian của vdv 1: "))
b = float(input("thời gian của vdv 2: "))
c = float(input("thời gian của vdv 3: "))

Dtb=(a+b+c)/3
print(f"thời gian trung bình là {Dtb}")
print("thời gian trung bình là ", round(Dtb, 2)) # round hàm làm tròn, 2 lấy 2 số