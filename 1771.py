n,x = map(int,input().split())
sp_p = list(map(int,input().split()))

res = 0
sp = []
for i in range(0,n):
    if sp_p[i] > 9:
        res+=1
    else:
        sp.append(10 - sp_p[i])
sp.sort()

i = 0
while i < len(sp) and x > 0:
    if x >= sp[i]:
        x -= sp[i]
        res += 1
    else:
        break
    i += 1

print(res)
