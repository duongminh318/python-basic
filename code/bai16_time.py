import time
giay= time.time()
print(giay)

hientai=time.ctime(0)
print(hientai)

print("moi nhap vao dap an: ")
# time.sleep((5))
print("het gio roi")

thoigian3=time.localtime()
print(thoigian3)
print("nam hien tai la: ",thoigian3.tm_year)
namhientai= thoigian3.tm_year
print("thang hien tai la: ",thoigian3.tm_mon)

t= time.localtime()
time_string= time.strftime("%m/%d/%y, %H:%M:%S", t)
print("string time: ", time_string)
print(type(time_string))

tuoi=int(input("moi cu nhap vao tuoi: "))
namsinh= namhientai- tuoi
print("nam sinh: ", namsinh)
print("nam dat 100 tuoi:", namsinh+100)