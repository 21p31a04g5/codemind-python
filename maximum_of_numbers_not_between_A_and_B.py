n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
l2=[]
for i in range(len(l)):
    if l[i]<a or l[i]>b:
        l2.append(l[i])
if len(l2)==0:
    print("-1")
else:
    print(max(l2))