n=int(input())
k=n
rev=0
while n:
    r=n%10
    rev=rev*10+r
    n=n//10
if k==rev:
    print("True")
else:
    print("False")
   
        