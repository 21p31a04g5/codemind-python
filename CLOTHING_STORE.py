n=int(input())
l=list(map(int,input().split()))
a=0
d={}
for i in l:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for i in d.values():
    a+=i//2
print(a)