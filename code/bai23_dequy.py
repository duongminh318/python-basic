# môt vài ví dụ sử dụng đệ quy
'''Đệ quy dùng khi :
1. Bài toán biết dc điểm dừng
2. Xác định dc quy luật
'''
# tinh n!
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# print(factorial(5))

# fibonaci
def fiBoNaCi(n):
    if(n==1 or n==2):
        return 1
    elif(n>2) :
        return fiBoNaCi(n-1)+ fiBoNaCi(n-2)
x= int (input("moi thim nhap so muon tính fibonaci: "))
f=fiBoNaCi(x)
print(f"fibonaci cua {x} : ", f)

for i in range(1,x+1,1):
    f = fiBoNaCi(i)
    print(f, end=" ")




