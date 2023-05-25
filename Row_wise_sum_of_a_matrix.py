a,b=map(int,input().split())
l=[list(map(int,input().split())) for i in range(a)]
for i in l:
    print(sum(i), end=' ')