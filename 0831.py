import math

m, n = map(int, input().split())
sp = [int(input()) for _ in range(n)]

def can(x):
    crav = 0
    for r in sp:
        v = (4 / 3) * math.pi * (r ** 3)
        crav += v // x
    return crav >= m

a, b = 1e-9, (4 / 3) * math.pi * (max(sp) ** 3)
while (b - a) >= 1e-4:
    c = (a + b) / 2
    if can(c):
        a = c
    else:
        b = c

res = (a + b) / 2
print(round(res * m, 4))
