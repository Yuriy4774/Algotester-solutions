n,m = map(int,input().split())
mx = [0] * m
for i in range(n):
    sp = list(map(int,input().split()))
    for j in range(m):
        if sp[j] > mx[j]:
            mx[j] = sp[j]
print(sum(mx))