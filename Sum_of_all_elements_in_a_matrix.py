a,b=map(int,input().split())
l=[list(map(int,input().split())) for i in range(a)]
s=0
for i in l:
    s+=sum(i)
print(s)