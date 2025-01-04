k,n = map(int, input().split())
sp = list(map(int, input().split()))
sp.sort()
res = 0

for i in sp:
    k-=i
    if k >= 0:
        res+=1
    else:
        break
print(res)

