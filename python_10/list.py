
from pip._vendor.rich import print

ds= [int(i) for i in input().split()]
sonho =0
for i in ds:
    if i<=100: sonho=sonho+1
print(sonho)