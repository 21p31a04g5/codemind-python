n=input()
e=0
o=0
for i in n:
    if int(i)%2==0:
        e+=1
    else:
        o+=1
if len(n)==e:
    print("Even")
elif len(n)==o:
    print("Odd")
else:
    print("Mixed")