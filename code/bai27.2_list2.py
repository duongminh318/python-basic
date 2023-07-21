# max_ min
lst= [1,3,4,2,6,4]
print("max of list : ",max(lst))
print("min of list : ",min(lst))
# lenght of list
print("lenght of list: ",len(lst))

#add an element into list (nối thêm)
lst.append(100)
print(lst)

lst.append("Hello python")
lst.append("Hello python")
print(lst)
#   count an elememt of list
count=lst.count("Hello python")
print(count)

#reverse list
lst.reverse()           #tự đảo nguược chính nó
print("The list after reverse: ",lst)

# insert the element into index of list
#listname.insert(index, element)
lst.insert(1, "insert into index 1")
print("list after insert: ",lst)


#find index of an element in list
a= lst.index(100)
print(f"Hello python index: {a} of list")

# insert a new list append old list from end
lst2= ["nối", 0, 3, 5, 9, 9]
lst.extend(lst2)
print(lst)

#reset list
lst.clear()
print(lst)

#18 sort the list (sap xep tang dan)
lst1 =[0, 3, 5, 9, 9 ,0, 8]                 #chi sap xep cho chinh no
lst1.sort()
print(lst1)

lst3=sorted(lst1)            # sap xep roi gan sang list moi
print(lst3)



