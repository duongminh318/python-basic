'''string= "hhhh4hello   he he"
a=string.strip("h")         #delete the chars in start and end of string
print(string)
print(a)
print(len(string))
print(len(a))

string.count('h')
print(string.count('he', 1, 10)) #count the chars in string

'''
#viet hoa ky tu dau
vidu="abc hello world"
print(vidu.capitalize())

# replace the string in string
listcrush= "Kieu Mai, Cuc, Dao, Hue, Kim Mai, Bao Mai"
print(listcrush)
#str.replace("old string ", "new string",count)
newlist= listcrush.replace("Mai","Huong", 2)
print(newlist)

#find the string the first show in string
print(listcrush.find("Mai", 9, 32 ))
print(listcrush[25:32])




