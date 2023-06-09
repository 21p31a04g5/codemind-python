n=input()
j=1
s=0
for i in n:
    s+=int(i)**j
    j+=1
if int(n)==s:
    print("True")
else:
    print("False")