a=list(input().split())
b='aeiouAEIOU'
c=0
for i in a:
    if i[0] in b and i[-1] not in b:
        c+=1
print(c)