n=list(input().split())
a='aeiou'
b=[]
for i in n:
    c=0
    for j in i:
        if j in a:
            c+=1
    b.append(c)
print(max(b))