n = int(input())
sp_o = list(map(int,input().split()))
sp_b = list(map(int,input().split()))

res = sum(sp_o)
b = 0
for i in range(0,n):
    a = b + sp_b[i]
    b+=sp_o[i]
    res = min(res,a)

print(res)
