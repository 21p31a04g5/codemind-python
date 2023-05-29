n=int(input())
a,b=0,1

l1 =[]
l1.append(a)
l1.append(b)
for i in range(1,n-1):
    c=a+b
    a=b
    b=c
    l1.append(c)
print(*l1, end = ' ')