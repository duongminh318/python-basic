a="""tôi chăm học
        tôi chịu khó
        tôi đẹp trai
        """
b=a.split()
print(b)
count =0
for i in b:
    if i=="tôi":
        count+=1
print(count)
