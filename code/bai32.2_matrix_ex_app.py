# 1. Viết chương trình nhập vào ma trận có m dòng và n cột
# (m, n do người dùng nhập từ bàn phím). Các phần tử ngẫu nhiên
# từ (1 đến 100
import random

row= int(input("Enter the number Row of matrix:"))
column= int(input("Enter the number Column of matrix:"))
matrix= []
for i in range(0,row,1):
    one_row=[]
    for j in range(0,column,1):
        one_row.append(random.randrange(0, 100))
    matrix.append(one_row)

for hang in matrix:
    for element in hang:
        print("{:<7}".format(element), end=" ")
    print()

#2. Xuất dòng bất kỳ nhập từ bàn phím
'''showrow= int(input("moi thim nhap vao dong muon xuat: "))
print(matrix[showrow])'''
# Xuất cột bất kỳ từ bàn phím
"""showcol= int(input("moi thim nhap vao cot muon xuat: "))
for col in matrix:
    print(col[showcol])"""
#4. Xuất số MAX trong ma trận trên
max = matrix[0][0]
for i in range(0,row,1):
    for j in range(0,column,1):
        if(max> matrix[i][j]):
            continue
        else:
            max= matrix[i][j]
print(max)