n, k = map(int, input().split())
sp = list(map(int, input().split()))

dp = []
a = []

for i in range(n):
    if sp[i] >= k:
        a.append(sp[i])
    else:
        if a:
            dp.append(a)
        a = []

if a:
    dp.append(a)

b = [len(t) for t in dp]

print(max(b) if b else 0)

