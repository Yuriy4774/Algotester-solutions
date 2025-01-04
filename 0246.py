n, m = map(int, input().split())
sp = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    sp[a].append(b)
    sp[b].append(a)

res = {}

for i in range(1, n + 1):
    if len(sp[i]) == 1:
        neig= sp[i][0]
        sp[sp[i][0]].append(0)
        if neig in res:
            res[neig] += 1
        else:
            res[neig] = 1

print(len(res))
