def abn(n):
    fs= sum([fctr for fctr in range(1, n) if n % fctr == 0])  
    return fs> n  
a = int(input())
if abn(a):  
    print("True");  
else:  
    print("False")  
    