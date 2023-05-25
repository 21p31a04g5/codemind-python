n=input()
c=0
a='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '
for i in n:
    if i not in a:
        c+=1
print(c)
        
    