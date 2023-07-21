a1= "python"
a2= 'Duong minh lập trình'
a3= """"bỗng muốn khóc cho lòng nhẹ nỗi đâu
        sau em không cứ khóc đi em"""
a4 = '''năm quan đổi lấy miệng cười
            mười quan anh chẳng tiếc
                chỉ tiếc người có duyên -_-'''

print(a1)
print(a2)
print(a3)
print(a4)

#một số hàm
print(len(a4))
#duyệt chuỗi
'''for i in a2:
    print(i, end="\t")'''
# cộng chuỗi
a= a1 +" "+ a2
print(a)

a5=a1*5
print(a5)

#kiểm tra xem 1 đoạn nào đó có nằm trong chuỗi không
print("Duong" in a2)
girl= "Trang, Loan, Mai, Xuyen"
doan= input("nhap vao ten phan doan: ")

if doan in girl :
    print("Doan dung roi")
else :
    print(" Sai cmnr")

