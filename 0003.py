n = int(input())
sp = list(map(int,input().split()))

SP,res = [],[]
for i in range(n):
    SP.append([sp[i],i+1])
SP.sort()
for i in SP:
    res.append(i[1])

print(*res)

