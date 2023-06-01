n=int(input())
l=list(map(str,input().split()))
l1 = []
for i in l:
    l1.append(int(i[::-1]))
print(*l1)