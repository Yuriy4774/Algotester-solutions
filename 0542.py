def area(x1, y1, x2, y2, x3, y3, x4, y4):
    a, b = min(x2, x4) - max(x1, x3), min(y2, y4) - max(y1, y3)
    if a < 0 or b < 0:
        return 0
    return a * b

n, m = map(int, input().split())
sp_n = []
for i in range(n):
    a, b, c, d = map(int, input().split())
    sp_n.append([a, b, c, d])

sp_m = []
for i in range(m):
    a, b, c, d = map(int, input().split())
    sp_m.append([a, b, c, d])

res = 0
q,w = 0,0
for i in range(n):
    for j in range(m):
        if res <= area(sp_n[i][0], sp_n[i][1], sp_n[i][2], sp_n[i][3],
                            sp_m[j][0], sp_m[j][1], sp_m[j][2], sp_m[j][3]):
                            q,w = i+1,j+1	
        res = max(res, area(sp_n[i][0], sp_n[i][1], sp_n[i][2], sp_n[i][3],
                            sp_m[j][0], sp_m[j][1], sp_m[j][2], sp_m[j][3]))

print(q,w)
