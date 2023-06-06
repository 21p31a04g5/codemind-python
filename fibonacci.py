n=int(input())
a,b=0,1
z=[]
z.append(a)
z.append(b)
for i in range(n-2):
    c=a+b
    a=b
    b=c
    z.append(c)
print(*z)