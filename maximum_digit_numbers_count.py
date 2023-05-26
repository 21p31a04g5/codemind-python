n=int(input())
l=list(map(int,input().split()))
b=[]
for i in l:
    a=abs(i)
    b.append(a)
v=max(b)
c=[]
for i in l:
    s=abs(i)
    if len(str(v))==len(str(s)):
        c.append(i)
print(*c)