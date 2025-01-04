n=int(input())
t=list(map(int,input().split()))
s=list(map(int,input().split()))
p=list(map(int,input().split()))
sp=[]
for i in range(n):
	sp.append(i)
sp.sort(key=lambda i:t[i])
res=[]
T=0
for i in sp:
	if t[i] >= T:
		T=t[i]+s[i]
		res.append(i+1)
	else:
		if T-t[i] <= p[i]:
			T+=s[i]
			res.append(i+1)
print(len(res))
print(*res)

