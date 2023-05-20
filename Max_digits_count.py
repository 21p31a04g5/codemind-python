n=int(input())
l=list(map(int,input().split()))
m=max(l)
c=0
for i in l:
    if len(str(m))==len(str(i)):
        c+=1
print(c)