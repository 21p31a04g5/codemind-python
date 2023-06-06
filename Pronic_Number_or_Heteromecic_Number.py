n=int(input())
c=[]
for i in range(n):
    if i*(i+1)==n:
        c.append(i)
if len(c)==1:
    print("YES")
else:
    print("NO")