sp1=list(map(int,input().split()))
sp2=list(map(int,input().split()))
sp1.sort()
sp2.sort()
for i in range(3):
	if sp1[i] > sp2[i]:
		print("No")
		exit()
print("Yes")
