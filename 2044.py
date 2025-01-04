from collections import defaultdict

n,m = map(int, input().split())
sp,d = [],defaultdict(lambda: 0)
for i in range(n):
    sp.append(list(map(int, input().split())))

for i in range(0,n):
    for j in range(0,m):
        d[sp[i][j]] += 1

res = []
for key, value in d.items():
    if value == 2:
        res.append(key)
print(len(res))
print(*res)
