n=int(input())
l=list(map(int,input().split()))
k=[]
for i in range(len(l)):
    if l[i]==l.count(l[i]):
        k.append(l[i])
if len(k)==0:
    print("-1")
m=list(set(k))
print(min(k),max(k))