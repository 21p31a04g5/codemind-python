n=int(input())
a,b=0,1
z=[]
z.append(a)
z.append(b)
for i in range(1000):
    c=a+b
    a=b
    b=c
    z.append(c)
if n in z:
    print("True")
else:
    print("False")