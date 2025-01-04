n = int(input())
sp = list(map(int,input().split()))
sp1=[]
for i in sp:
	if i > 0:
		sp1.append(i)
sp = sp1
print(len(list(set(sp))))
	
