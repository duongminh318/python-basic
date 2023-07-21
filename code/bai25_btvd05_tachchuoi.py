n= input("Enter the String: ")
letter=""
num=""
for i in n:
    if i.isalpha():
        letter+=i
    elif i.isnumeric():
        num+=i
print(letter)
print(num)

