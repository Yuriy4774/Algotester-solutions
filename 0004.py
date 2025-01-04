n = int(input())
sp = list(map(int, input().split()))
sp1 = list(map(int, input().split()))
SP,res = [],[]
for i in range(n):
    SP.append([sp1[i]/sp[i],i+1])
SP.sort(reverse=True)
for i in range(n):
    res.append(SP[i][1])
print(*res)

