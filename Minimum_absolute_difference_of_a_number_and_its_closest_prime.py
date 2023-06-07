import math
def pr(a):
    if a==1:
        return False
    else:
        for i in range(2,int(math.sqrt(a))+1):
            if a%i==0:
                return False
        return True
n=int(input())
b=[]
for i in range(0,n+1):
    if pr(i):
        b.append(i)
for i in range(n+1,n**2):
    if pr(i):
        b.append(i)
        break
if n-b[-2]<b[-1]-n:
    print(n-b[-2])
else:
    print(b[-1]-n)