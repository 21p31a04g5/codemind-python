n=int(input())
l=list(map(int,input().split()))
c=0
p=[]
for i in range(len(l)):
    if l[i]==l.count(l[i]):
        p.append(l[i])
a=set(p)
print(len(a))