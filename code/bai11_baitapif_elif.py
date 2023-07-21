# bth5: kiểm tra số chẵn lẻ
'''n= int(input("mời cụ nhập vào một số nguyên: "))
if n%2==0:
    print(f"{n} là số chẵn")
else :
    print(f"{n} là số lẻ")'''
# bth6: xếp loại học sinh
'''diem= float(input("mời cụ nhập vào điểm trung bình: "))
if(diem<0 or diem> 10):
    print("điểm nhập vào không không hợp lệ")
elif diem>=9:
    print("loại giỏi, diem trung binh cua ban la: ",diem)
elif diem<9 and diem>=7 :
    print("loại khá, diem trung binh cua ban la:", diem)
elif diem>=5 and diem<7 :
    print("loại trung bình, diem trung binh cua ban la:", diem)
else:
    print("loại yếu diem trung binh cua ban la:", diem)'''
# bth7: viet chuong trinh kiem tra nam nhuan
'''nam= int(input("mời cụ vao nam: "))
if((nam%4 == 0 and nam%100 != 0) or nam%400 == 0):
    print(f"{nam} là nam nhuan")
else:
    print(f"{nam} là nam khong nhuan")'''
# bth8: viet chuong trinh dem so ngay trong thang
'''thang= int(input("moi cu nhap vao thang: "))
if(thang in (1, 3, 5, 7, 8, 10, 12)):
    print(f"{thang} co 31 ngay")
elif(thang in (4, 6, 9, 11)):
    print(f"{thang} co 30 ngay")
elif(thang==2):
    nam2= int(input("moi cu nhap them nam: "))
    if((nam2%4==0 and nam2%100!=0) or (nam2%400==0)):
        print(f"{thang} co 29 ngay")
    else:
        print(f"{thang} co 28 ngay")
else:
    print("thang vua nhap khong hop le")'''''
# bth9: viet chuong trinh giai pt bac 2
# bth10: viet chuong trinh kiem tra thang trong nam thuoc quy may
'''thang2= int(input("moi cu nhap vao thang: "))
if(thang2 in(1, 2, 3)):
    print(f"{thang2} thuoc quy 1")
elif(thang2 in(4, 5, 6)):
    print(f"{thang2} thuoc quy 2")
elif(thang2 in(7, 8, 9)):
    print(f"{thang2} thuoc quy 3")
elif(thang2 in(10, 11, 12)):
    print(f"{thang2} thuoc quy 4")
else:
    print(f"{thang2} khong ton tai")'''
# bth11: viet chuong trinh giai pt bac 2
import math

# nhập các hệ số a, b, c từ bàn phím
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

# tính delta
delta = b**2 - 4*a*c

# giải phương trình
if delta < 0:
    print("Phương trình vô nghiệm.")
elif delta == 0:
    x = -b / (2*a)
    print(f"Phương trình có nghiệm kép x = {x}.")
else:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print(f"Phương trình có hai nghiệm phân biệt: x1 = {x1}, x2 = {x2}.")

