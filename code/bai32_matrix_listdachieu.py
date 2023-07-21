from random import randrange

#define a matrix
'''matrix=[
    [1, 5, 8],
    [5, 8, 9],
    [9, 7, 8],
    [4, 7, 5]
]

for hang in matrix:
    for element in hang:
        print("{:<7}".format(element), end=" ")
    print()
'''
# create list quick
'''dong=4
cot=5
matrix2=[[1]*cot]*dong

for i in matrix2:
    print(i)'''

# create matrix random
arr=[]
row=int(input("Enter the number row of matrix: "))
column=int(input("Enter the number Colum of matrix: "))
for i in range(0,row,1):
    onerow=[]
    for j in range(0, column, 1):
         onerow.append(randrange(0, 21))
    arr.append(onerow)
print(arr)