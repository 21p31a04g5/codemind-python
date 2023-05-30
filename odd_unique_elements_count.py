n=int(input())
l=list(map(int,input().split()))
c=0
b=[]
for i in l:
    if i not in b:
        b.append(i)
for j in b:
    if j%2!=0:
        c+=1
print(c)