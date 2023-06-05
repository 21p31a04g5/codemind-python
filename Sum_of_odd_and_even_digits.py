n=int(input())
l=list(map(int,input().split()))
a=[]
b=[]
for i in range(n):
    if i%2 ==0:
        a.append(l[i])
    else:
        b.append(l[i])
if (sum(a)-sum(b)) == 0:
    print("YES")
else:
    print("NO")