n, m = map(int, input().split())
sp = []
for i in range(n):
    sp.append(list(map(int, input().split())))

ind = -1
max_a = float('inf')
for i in range(m):
    a = 0
    for j in range(n):
        if sp[j][i] > a:
            a = sp[j][i]
    if a < max_a:
        max_a = a
        ind = i
res = float('-inf')
for i in range(n):
    if sp[i][ind] > res:
        res = sp[i][ind]
print(res)