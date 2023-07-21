"""import  math
pi= math.pi
r= float(input("mời nhập vào bán kính r: "))
chuvi = 2*pi*r
dientich= pi*(r**2)
print("chu vi hình tròn là: ", chuvi)
print("diện tích hình tròn là: ", dientich)"""

import math

radius = float(input("Enter the radius of the circle: "))

def circle_area(r):
    return math.pi * r ** 2

def circle_circumference(r):
    return 2 * math.pi * r
# xuất kiểu 1
print(f"Area of the circle: {circle_area(radius)} " )

# xuât kiểu 2
print("Circumference of the circle: ", circle_circumference(radius))

# kiểu 3
print("chu vi la {} dien tích là {}".format(circle_area(radius), circle_circumference(radius) ))
