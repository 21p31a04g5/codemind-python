n=int(input())
c=[]
for i in range(n):
    if i*i==n:
        c.append(i)
if len(c)==1:
    print("True")
else:
    print("False")