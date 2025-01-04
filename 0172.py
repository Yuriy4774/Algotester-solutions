n,m,k = map(int,input().split())
sp = list(map(int,input().split()))

res = n
a = 0
for i in range(0,m):
    if a + sp[i] <= k:
        a+=sp[i]
    else:
        a = 0
        res-=1
print(res)