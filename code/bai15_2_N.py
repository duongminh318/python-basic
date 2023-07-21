# N nghiêng trái
'''height= int(input("enter the height:"))
for i in range(height):
    for j in range(height):
        if(j==0 or j==height-1 or i+j==height-1):
             print("*", end=" ")
        else :
            print(" ", end=" ")
    print()
'''

# N nghieng phai
'''height= int(input("enter the height:"))
for i in range(height):
    for j in range(height):
        if(j==0 or j==height-1 or i==j):
             print("*", end=" ")
        else :
            print(" ", end=" ")
    print()'''

# ve hinh trai tim
for i in range(7):
    for j in range(7):
        if((i==0 and j in(1,2,4,5)) or
                (i==1 and j in (0,3,6)) or
                (i==2 and j in (0,6)) or
                (i==3 and j in (1,5)) or
                (i==4 and j in(2,4)) or
                (i==5 and j==3)):
                    print("*", end="  ")
        else:
            print("  ", end="  ")


    print(" ")