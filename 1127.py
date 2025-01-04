n=int(input())
sp=input()
res=0
a=sp[0]
c=1
for i in range(1,n):
	if sp[i]==a:
		c+=1
	else:
		res=max(res,c)
		c=1
		a=sp[i]
res=max(res,c)
print(n-res)
