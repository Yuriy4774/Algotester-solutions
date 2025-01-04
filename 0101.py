n, m = map(int, input().split())
sp = []
for i in range(n):
    sp.append(list(input()))

sp_orig = [row[:] for row in sp]

for i in range(n):
    a = {}
    for j in sp_orig[i]:
        if j in a:
            a[j] += 1
        else:
            a[j] = 1
    
    b = []
    for j in sp_orig[i]:
        if a[j] == 1:
            b.append(j)
        else:
            b.append('.')
            a[j] = 0
    
    sp[i] = b

for j in range(m):
    a = {}
    for i in range(n):
        if sp_orig[i][j] in a:
            a[sp_orig[i][j]] += 1
        else:
            a[sp_orig[i][j]] = 1

    for i in range(n):
        if a[sp_orig[i][j]] > 1:
            sp[i][j] = '.'

res = ""
for i in range(n):
    for j in range(m):
        if sp[i][j] != '.':
            res += sp[i][j]
print(res)
