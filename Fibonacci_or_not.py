n=int(input())
a,b=0,1
x=[]
x.append(a)
x.append(b)
for i in range(1000):
    c=a+b
    a=b
    b=c
    x.append(c)
if n in x:
    print("True")
else:
    print("False")