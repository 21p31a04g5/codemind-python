n=int(input())
a=n*n
c=0
while a>0:
    c=c+a%10
    a=a//10
if n==c:
    print("Neon Number")
else:
    print("Not Neon Number")