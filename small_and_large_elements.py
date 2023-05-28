n=list(input().split())
for i in n:
    if i in n[0] and n[-1]:
        continue
print(min(n[0]),max(n[-1]))
    