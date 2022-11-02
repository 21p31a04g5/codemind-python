n=int(input())
sum=0
for i in range (1,n+1):
    if i*i==n:
        print("True")
        sum=1
        break
if sum==0:
        print("False")
        
    