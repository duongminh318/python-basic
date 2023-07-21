n= int(input("Enter numbers of list: "))
list=[0]*n
count=0
temps=""
for i in range(0,n,1):
    a=int(input(f"enter for element {i+1}: "))
    list[i]= a
    # print (> 5)
    if(list[i]>5):
        count+=1
        temps+=str(i)+"; "

print("so phan tu lon hon 5: ",count)
print("vi tri index lon hon 5: ",temps)
