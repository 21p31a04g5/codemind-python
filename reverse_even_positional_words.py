n=input().split()
a=0
l=[]
for i in n:
    if a%2==0:
        l.append(i[::-1])
    else:
        l.append(i)
    a+=1
print(*l)
        