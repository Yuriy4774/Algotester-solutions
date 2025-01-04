# a, b = map(int, input().split())
a = list(input())
b = list(input())
sp = []
res = []
sp = [[0]*(len(b)+1) for _ in range(len(a)+1)]
for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        if a[i-1] == b[j-1]:
            sp[i][j] = sp[i-1][j-1] + 1
        else:
            sp[i][j] = max(sp[i-1][j],sp[i][j-1])

i, j = len(a), len(b)
while i > 0 and j > 0:
    if a[i-1] == b[j-1]:
        res.append(a[i-1])
        i-=1
        j-=1
    else:
        if sp[i-1][j] > sp[i][j-1]:
            i-=1
        else:
            j-=1
res = res[::-1]
if res:
    s = ""
    for i in res:
        s += i

    print(s)

else:
    print("No original genome")
