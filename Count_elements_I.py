a,b=map(int,input().split())
l=list(map(int,input().split()))
k=list(map(int,input().split()))
c=len(set(l) & set(k))
print(str(c))