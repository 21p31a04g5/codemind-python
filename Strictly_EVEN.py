n=int(input())
l=list(map(int,input().split()))
f=0
for i in range (len(l)):
    if l[i]%2==0 and i%2!=0:
        f+=1
        print("False")
        break
if f==0:
    print("True")
     
