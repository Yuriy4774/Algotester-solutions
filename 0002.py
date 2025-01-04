n = int(input())
sp = list(map(int, input().split()))
dp = [1] * len(sp)
for i in range(0, len(sp)):
    for j in range(0, i):
        if sp[i] > sp[j]:
            dp[i] = max(dp[i], dp[j] + 1)


print(max(dp))
