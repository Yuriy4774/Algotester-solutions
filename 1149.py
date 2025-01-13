m,n,k = map(int,input().split())
d = dict()
for i in range(m):
    a,b = map(str,input().split())
    d[a] = int(b)
sp = dict()
for i in range(n):
    a = input()
    res = 0
    for j in a:
        res+=d[j]
    if res <= k:
        sp[a] = res

mx = max(sp.values())
res = []
for x,y in sp.items():
    if y == mx:
        res.append(x)
#print(res)
res.sort()
print(res[0])