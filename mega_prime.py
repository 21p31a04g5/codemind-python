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
if pr(n):
    f=0
    while n:
        r=n%10
        if pr(r)==False:
            f+=1
            print("Not Mega Prime")
            break
        n=n//10
    if f==0:
        print("Mega Prime")
else:
    print("Not Mega Prime")