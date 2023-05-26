n,m=map(int,input().split())
l=list(map(int,input().split()))
c=0
for i in l:
    a=abs(i)
    if len(str(a))==m:
        c+=1
print(c)