n=int(input())
c=[]
for i in range(1,n):
    if n%i==0:
        c.append(i)
if sum(c)>n:
    print("True")
else:
    print("False")