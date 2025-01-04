n = int(input())
sp = list(map(int, input().split()))
x = int(input())

s = sum(sp)
res = s / n
while s >= x:
    a = min(sp)
    sp.remove(a)
    s = sum(sp)
    if s >= x:
        res = max(res,s / len(sp))

print(res)
