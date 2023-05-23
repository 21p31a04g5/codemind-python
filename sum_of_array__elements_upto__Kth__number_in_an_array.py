n=int(input())
l=list(map(int,input().split()))
m=int(input())
v=[]
for i in l:
    if i<=m:
        v.append(i)
print(sum(v))