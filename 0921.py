a, b = map(int, input().split())
a,b = min(a,b),max(a,b)
c = a+1
if c < b:
    print(c)
else:
    print(-1)

