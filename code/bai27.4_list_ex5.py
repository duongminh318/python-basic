n= int(input("Enter numbers of list: "))
lst_max=[]
lst_min=[]
lst=[0]*n
# print(lst)
for i in range(0,n,1):

    a= int(input(f"moi thim nhap gia tri cho phan tu thu {i+1}: "))
    lst[i] = a
for i in range(0,n,1):
   if lst[i]==max(lst):
       continue
   else:
       lst_max.append(lst[i])
   if lst[i] == min(lst):
       continue
   else:
       lst_min.append(lst[i])
print(lst)
print("gia tri lon thu 2 trong list : ",max(lst_max))
print("gia tri nho thu 2 trong list : ",min(lst_min))
