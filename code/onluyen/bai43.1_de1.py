#get n
with open("tong.imp")as f2:
    n=int(f2.read())
print(n)
print(type(n))

tong=0
for i in range(1,n+1):
    tong+=1/(i**2)
print(round(tong,3))
s=str(round(tong,3))
s=s.replace(".",",")
with open("tong.out","w") as out:
    out.write(s)