n,m = map(int,input().split())

sp_r = []
for i in range(n):
    radok = list(input())
    sp_r.append(radok)

sp_s = []
for i in range(m):
    stovp = []
    for j in range(n):
        stovp.append(sp_r[j][i])
    sp_s.append(stovp)
def check(r,s):
    for i in r:
        if i == '1':
            return False
    for i in s:
        if i == '1':
            return False
    return True
for i in sp_r:
    for j in sp_s:
        if check(i,j):
            print("NO")
            exit()
print("YES")
