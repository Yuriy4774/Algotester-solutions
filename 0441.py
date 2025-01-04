n,k = map(int,input().split())
sp = list(map(int,input().split()))

sp.sort()
res = float('inf')
for i in range(0,n-k+1):
    res = min(sp[i+k-1]- sp[i],res)
print(res)