n=int(input())
a,b=0,1
x=[]
x.append(a)
x.append(b)
for i in range(n-2):
    c=a+b
    a=b
    b=c
    x.append(c)
print(*x)