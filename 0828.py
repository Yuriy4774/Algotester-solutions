n = int(input())
sp = list(map(int, input().split()))
res = 0

for i in range(1,n+1):
    res += sp[i-1] * (n-(i-1))

print(res)
