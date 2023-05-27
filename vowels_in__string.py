n=input()
m='aeiouAEIOU'
a=[]
for i in n:
    if i in m:
        if i not in a:
            a+=i
if len(a)==0:
    print(-1)
else:
    print(*a)