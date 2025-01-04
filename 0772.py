n, m = map(int, input().split())

sp = []
for i in range(n):
    row = list(map(int, input().strip()))  
    sp.append([0] + row + [0])  
#add zeros
sp.insert(0, [0] * (m + 2))
sp.append([0] * (m + 2))

def count():
    c = [0] * 8  
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            c[sp[i][j]] += 1
    return c

def check(x, y):
    a = sp[x][y]
    if sp[x + 1][y] == a or sp[x - 1][y] == a or sp[x][y + 1] == a or sp[x][y - 1] == a or sp[x + 1][y + 1] == a or sp[x + 1][y - 1] == a or sp[x - 1][y + 1] == a or sp[x - 1][y - 1] == a:
        return True
    return False

total = count()

sus = [0] * 8  
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if check(i, j):
            sus[sp[i][j]] += 1

for i in range(1, 8):
    print(f"{i} - {total[i]} {sus[i]}")

