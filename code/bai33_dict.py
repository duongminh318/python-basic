d= {"Tung" : 1.65, "Tuan" : 1.64, "Linh" : 1.60 } # giá trị lặp lại {'một': 1, 'hai': 2, 'ba': 2}
print(d)
dic2={"một" : 1, "một" : 2, "ba" : 2 }
print(dic2)
#dict long nhau
dic3 = {'office':{ 'room1':'Finance ', 'room2':'logistics'},
 'lab':{'lab1':'Physics', 'lab2':'Chemistry'}}
print(dic3["office"]["room1"])

# sua hoac them key vao dict
d["Tung"]=1.7
print(d)
d["Hung"]=1.85
print(d)

del d["Hung"]
print(d)
# del d
print(d)
print(len(d))
