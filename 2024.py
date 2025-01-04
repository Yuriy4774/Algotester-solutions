n = int(input())
sp = map(int,input().split())
p = int(input())
res = 0
l,r = p,p
for i in sp:
    l1,r1 = i,i+1
    if l1 > r or r1 < l:
        res+=0
    else:
        l = min(l,l1)
        r = max(r,r1)
        res+=1
print(res)
