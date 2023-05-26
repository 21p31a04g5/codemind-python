a=input()
b='aeiou'
c=''
for i in a:
    if i in b:
        c+=i
d=''
for i in b:
    if i not in c:
        d+=i
if len(d)==0:
    print(0)
else:
    for i in d:
        print(i,end=' ')

        
