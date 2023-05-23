n=int(input())
l=list(map(int,input().split()))
k=[]
for i in l:
    if i==l.count(i):
        if i not in k:
            k.append(i)
if len(k)==0:
    print("-1")
else:
    print(*k)