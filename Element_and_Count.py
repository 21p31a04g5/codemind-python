n=int(input())
l=list(map(int,input().split()))
c=[]
for i in l:
    if i not in c:
        c.append(i)
for j in c:
    print(j,l.count(j),end=' ')