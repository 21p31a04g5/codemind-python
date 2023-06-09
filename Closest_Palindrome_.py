def pl(a):
    if str(a)==str(a)[::-1]:
        return True
n=int(input())
c=[]
for i in range(n):
    if pl(i):
        c.append(i)
for i in range(n+1,n**2):
    if pl(i):
        c.append(i)
        break
if n-c[-2]<c[-1]-n:
    print(c[-2])
elif n-c[-2]==c[-1]-n:
    print(c[-2],c[-1])
else:
    print(c[-1])