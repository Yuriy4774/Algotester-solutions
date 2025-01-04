n = int(input())
sp = []

def time_to_seconds(h, m, s):
    return (h - 8) * 3600 + m * 60 + s
SP = [False] * 43200

for i in range(n):
    sp.append(input().split())
for i in range(n):
    for j in range(6):
        if sp[i][j][0] == '0':
            sp[i][j] = sp[i][j][1]
        sp[i][j] = int(sp[i][j])

for i in range(n):
    a,b = time_to_seconds(sp[i][0],sp[i][1],sp[i][2]),time_to_seconds(sp[i][3],sp[i][4],sp[i][5])
    #print(a,b)
    for i in range(a,b):
        SP[i] = True

print(SP.count(False))
