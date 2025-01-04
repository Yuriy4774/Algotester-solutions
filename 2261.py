n = int(input())
sp = list(map(int,input().split()))

res = 0
for i in range(0,n-1):
    res = max(res,sp[i]*sp[i+1])
print(res)
