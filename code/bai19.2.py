'''height= int(input("enter the height:"))
def Nnghientrai(height):
    for i in range(height):
        for j in range(height):
            if(j==0 or j==height-1 or i+j==height-1):
                 print("*", end=" ")
            else :
                print(" ", end=" ")
        print()

def Nnghienphai(height):
    for i in range(height):
        for j in range(height):
            if(j==0 or j==height-1 or i==j):
                 print("*", end=" ")
            else :
                print(" ", end=" ")
        print()

if(height%2==0):
    Nnghienphai(height)
else:
    Nnghientrai(height)'''

# bai tap roi
def tinhRoi(doanhthu, chiphi):
    return  (doanhthu-chiphi)/chiphi

def quetDinhDauTu(roi):
    if(roi>=0.75):
        print("Thim nen dau tu ")
    else:
        print("Thim Khong nen dau tu ")

a = float(input("moi thim nhap doanh thu: "))
b = float(input("moi thim nhap chi phi: "))
c = tinhRoi(a, b)
print("he so Roi= ", c)
quetDinhDauTu(c)

