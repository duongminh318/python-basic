string ="aASHINA"
print(len(string))
'''print(string[7])'''
a= len(string)
print(string[-7])
string ="aASHINA"
for i in range(-1, a-1, -1): #den gan sat -8 tuc la lap den luc <=(-8) thi dung
    print(string[i], end="")
print(string)


print(string[1:7:2])    #tư 1 đến sát 7 bước nhảy là 2
print(string[3])        # ký tự thư 3
print(string[1:6])      #  kt từ 1 đén sát 6
print(string[3:])       # từ 3 đến hết chuỗi
print(string[:3])       # từ đầu đê 3
print(string[:-1])          # chuỗi đảo ngược

t='''b12345e'''
print(t[0], t[-1])
print(t[1::2])
