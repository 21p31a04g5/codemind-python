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
m=int(input())
c=0
for i in range (n,m+1):
    if pr(i):
        c+=1
print(c)