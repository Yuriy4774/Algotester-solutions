n,t = map(int, input().split())
sp = list(map(int, input().split()))
res = 0
for i in range(1,len(sp)):
    a = abs(sp[i] - sp[i-1])
    res += a * t
print(res)
