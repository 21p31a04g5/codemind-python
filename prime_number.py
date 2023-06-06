n=int(input())
c=[]
for i in range(1,n+1):
    if n%i==0:
        c.append(i)
if len(c)==2:
    print("prime")
else:
    print("not a prime")
        