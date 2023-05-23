n=int(input())
l=list(map(int,input().split()))
a=sum(l)//n
b=[]
for i in l:
    if i <= a:
        b.append(i)
print(len(b))        
