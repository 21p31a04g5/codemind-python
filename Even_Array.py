n=input()
l=list(map(int,input().split()))
f=0
for i in range(len(l)):
    if i%2==0 and l[i]%2!=0:
        f+=1
        print("False")
        break
if f==0:
    print("True")