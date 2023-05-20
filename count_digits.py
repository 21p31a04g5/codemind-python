n=int(input())
l=list(map(int,input().split()))
for i in l:
    a=str(i)
    b=len(a)
    if(i<0):
        b-=1
    print(b,end=' ')