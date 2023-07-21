# cách 1
'''n= int(input("Enter numbers of list: "))
list=[0]*n
for i in range(0,n,1):
    a=int(input(f"enter for element {i+1}: "))
    list[i]= a
list2=[0]*n
count= 0
for i in range(0,n,1):
    list2[i]= list[i]*list[i]
    if(list2[i]>50):
        count+=1;
print("original list: ",list)
print("squared list: ",list2)
print("number of elements greater than 50 : ", count)'''
#cách 2
lst2=[]
n=int(input("Enter the number element of list: "))
count=0
while count<n:
    print(count)
    count= count+1

    a= int(input( f"Enter the elemnt {count}: "))
    print(a)
    lst2.append(a)
    print(lst2)
