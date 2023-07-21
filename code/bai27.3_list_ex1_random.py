import random

n= int(input("Enter numbers of list: "))
list=[0]*n
for i in range(0,n,1):
    list[i]= random.randrange(0,101) # số ngâu nhiên từ 0 đến xat 101
print(list)