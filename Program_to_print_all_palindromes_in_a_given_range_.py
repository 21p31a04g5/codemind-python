n=int(input())
m=int(input())
for i in range(n,m+1):
    i=str(i)
    if i==i[::-1]:
        print(int(i),end=' ')