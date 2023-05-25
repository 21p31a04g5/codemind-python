a=input()
l=[]
for i in a:
    if i not in l:
        l.append(i)
if len(l)==len(a):
    print("True")
else:
    print("False")