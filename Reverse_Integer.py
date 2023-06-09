n=int(input())
n=str(n)
if n[-1]==0:
    n.remove(n[-1])
n=int(n)
if n<0:
    n=str(abs(n))
    n=n[::-1]
    print(int("-"+n))
else:
    n=str(n)
    print(int(n[::-1]))
    