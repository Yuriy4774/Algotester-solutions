n=int(input())
res=n-1
while True:
	a,b = map(int,input().split())
	if a == 0 and b == 0:
		break
	elif a != b:
		res-=1
print(res)
