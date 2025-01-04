n = int(input())
n = input()
ln = len(n)

res = 1
for i in range(0,ln):
    l,r = i-1,i+1
    while l >= 0 and r < ln and n[r] == n[l]:
        l-=1
        r+=1
    res = max(res,r - l - 1)


for i in range(0,ln):
    l,r = i,i+1
    while l >= 0 and r < ln and n[r] == n[l]:
        l-=1
        r+=1
    res = max(res,r - l - 1)

print(res)
