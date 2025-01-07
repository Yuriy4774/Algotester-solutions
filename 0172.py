n,m,k=map(int,input().split())
sp = list(map(int,input().split()))
c=0
res=0
for i in range(m):
	if c + sp[i] > k:
		res+=1
		c=0
	c+=sp[i]
if c != 0:
	res+=1
if res <= n:
	print(n-res)
else:
	print(-1)
