n,k,x=map(int,input().split())
sp=list(map(int,input().split()))

K=0
for i in sp:
	if i > k:
		K+=1
if x+1>=K:
	print("YES")
	exit()
print("NO")
