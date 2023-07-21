def cong(x,y):
    return x+y

def tru(x,y):
    return "hieu={}".format(x-y)

def ptbac1(a,b):
    if(a==0 & b==0):
        print("pt vo so nghiem")
    elif(a==0):
        print("pt vo nghiem")
    elif(b==0):
        print("pt co nghiem x=0")
    else:
        print("pt co nghiem x= ",(-b)/a)

# ham khong return
chuoi=input(" nhap chuoi: ")
def Xuatchuoi(string):
    print("ham xuat chuoi ra: ", chuoi)


print(cong(3,4))
print(tru(4,2))
print(tru(cong(3,4),2))
ptbac1(0,0)
Xuatchuoi(chuoi)