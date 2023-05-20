n=int(input())
l=list(map(int,input().split()))
k=[]
c=0
for i in l:
    if i%2==0 and i not in k:
        k+=[i]
        c+=1
print(c)