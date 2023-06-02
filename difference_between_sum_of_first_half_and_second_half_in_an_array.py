n=int(input())
l=list(map(int,input().split()))
l1=l[:n//2]
l2=l[n//2:n]
print(sum(l2)-sum(l1))