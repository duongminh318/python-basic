'''from random import randrange
a= randrange(3)     #random  <3 (0, 1, 2)
print(a)

b= randrange(3,10)  # 3<random<10
print(b)'''

import random
a = random.randrange(1,10)
i = 3
while True:
    b = int(input("your number is: "))
    if b != a:
        i-=1
        if b > a:
            print("your number is higer")
        else:
            print("your number is lower")
        print("wrong! If you enter incorrectly more than three times, you will be locked,your remaining turn is",str(i))
        if i == 0:
            print("you lose good bye")
            break
    else:
        print("you win! congratulation")
        break