n = int(input())
sp = list(map(int,input().split()))
sp.sort()
res = "YES"
for i in range(1,len(sp)):
    if sp[i] - sp[i-1] >= 2:
        continue
    else:
        res = "NO"
        break
print(res)
