n=int(input())
m=int(input())
a=[]
b=[]
for i in range(1,n):
    if n%i==0:
        a.append(i)
for i in range(1,m):
    if m%i==0:
        b.append(i)
if sum(a)==m or sum(b)==n:
    print("Amicable")
else:
    print("Not Amicable")