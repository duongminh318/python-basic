n= int(input("Enter numbers of list: "))
list = [0]*n
list = [1,2,3,4, "ahihi",'do ngoc',"""ahihi do ngoc"""]
list2 = ["excel", 1, 3, "computer"]
list3 = [list, list2]
# print(type(list))
print(list)
print(list2)
print(list3[1][0])

# ham
'''list4 = [0, 1, 2, 3, 4, 5]
# print(len(list4))
print(list4[1:5])'''

# xuat nguoc list
lst = [3, 8, 9, 2, 4]

for i in range(len(lst)-1,-1 ,-1): #range (begin, end, step) ket thuc khi sat gan -1
    k= lst[i]
    print(k, end=" ")
print()
# xu ly
print(lst)
lst[0] = "python" #thay thế giá trị tại index nào đó
print(lst)
del lst[1]          #xoá giá trị tại index nào đó
print(lst)
lst.remove("python")        #xoá giá trị trong list
print(lst)

# del lst             #xoá all list
# print(lst)
