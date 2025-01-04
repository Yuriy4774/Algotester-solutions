n = input()
sp = []
minn,maxn = "","".join(sorted(n,reverse=True))
for i in range(0,10):
    sp.append(n.count(str(i)))
k = 1
for i in range(1,10):
    if sp[i] > 0:
        k = i
        break
minn+=str(k)
for i in range(0,10):
    if i  == k:
        for j in range(sp[i]-1):
            minn+=str(i)
    else:
        for j in range(sp[i]):
            minn+=str(i)
print(minn,maxn)
