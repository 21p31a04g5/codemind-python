n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(len(l)-1):
    if l[i]<l[i+1]:
        print("no")
        c=1
        break
if c==0:
    print("yes")