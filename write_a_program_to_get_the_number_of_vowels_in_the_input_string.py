n=input()
m='aeiouAEIOU'
a=0
for i in n:
    if i in m:
        a+=1
print(a)