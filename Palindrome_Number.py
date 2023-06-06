n=int(input())
for i in range(n):
    m=int(input())
    k=str(m)
    a=k[::-1]
    b=int(a)
    if m==b:
        print("True")
    else:
        print("False")