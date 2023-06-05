n=int(input())
for i in range(n):
    s=input()
    def fun(s):
        return 'Yes' if set(s).intersection('0123456789') else 'No'
    print(fun(s))        