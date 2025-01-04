n,m,k=map(int,input().split())
sp = list(map(int,input().split()))
for i in range(n):
	sp[i] = sp[i] * 2
sp.sort()
a = min(n,m)
i = 0
while i < a and k - sp[i]>= 0:
	k-=sp[i]
	i+=1
print(i)
