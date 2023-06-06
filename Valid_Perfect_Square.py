n=int(input())
for i in range(n):
    c=[]
    m=int(input())
    for j in range(m):
        if j*j==m:
            c.append(j)
    if len(c)==1:
        print("True")
    else:
        print("False")
        