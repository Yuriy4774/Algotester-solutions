n=int(input())
sp1=list(map(int,input().split()))
sp2=list(map(int,input().split()))
sp3=list(map(int,input().split()))
sp=[sp1,sp2,sp3]
res=float('inf')
for i in range(3):
	for j in range(3):
		if i != j:
			a=0
			for k in range(n):
				a+=min(sp[i][k],sp[j][k])
			res=min(res,a)
			
print(min(res,sum(sp1),sum(sp2),sum(sp3)))			
