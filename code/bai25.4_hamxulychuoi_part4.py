string= "ahihi"
string1= "=*#$%"
print(string.isalnum())         #chi chua so hoac chu
print(string1.isalnum())

str= "123"
str2= "dafafdaa"
print(str.isdigit())        #chi chua so
print(str2.isdigit())

print(str2.isalpha())

strthuong= "Chu nAo Viet tHuong sau Chuyen thanh hoa hoac nguoc lai"
tempstring=""
print(strthuong)
for i in strthuong:
    if i.islower():
        i=i.upper()
    else:
        i=i.lower()
    tempstring+=i
print(tempstring)

demosplit= "Duong Khoi Minh; Dep trai vl; hocgioi; nhieu tien; nghia hiep"
arrlist= demosplit.split(";")
print(arrlist)
print(arrlist[0]+arrlist[4] + arrlist[1])
#duyet mang moi tach tao duoc
for i in arrlist:
    print(i)
#noi string trong mang moi element la mot string
a2=",".join(arrlist)
print(a2)

#bt vd
bt1= "university of technology and education"
print("a xuat hien o vi tri", end=": ")
for i in range(0, len(bt1), 1):
    if bt1[i]=="a":
        print(i, end=" ")

'''bt2= input("moi thim nhap vao string muon double: ")
tempstring2= ""
for i in bt2:
    tempstring2=tempstring2+i+i
print(tempstring2)'''
#dem so nguyen am in string (u e o a i)
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

s = input("Nhập vào một chuỗi: ")
num_vowels = count_vowels(s)
print("Số lượng nguyên âm trong chuỗi là:", num_vowels)




