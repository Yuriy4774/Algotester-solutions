sp = list(map(int,input().split(", ")))
res = 0
sp.sort()
while True:
    if len(sp) < 4:
        break
    a,b = sp[0] + 2*sp[1] + sp[len(sp)-1],2*sp[0]+sp[len(sp)-2]+sp[len(sp)-1]
    res+=min(a,b)
    sp.pop(-1)
    sp.pop(-1)
if len(sp) == 2:
    res+=max(sp)
elif len(sp) == 3:
    res+=sum(sp)
elif len(sp) == 1:
    res+=sp[0]
print(res)