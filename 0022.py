import math

n = int(input())
sp = list(map(int,input().split()))

def gccd(sp):
	a = sp[0]
	for i in range(1,len(sp)):
		a = math.gcd(a,sp[i])
	return a
res = 0
gcdd = gccd(sp)
for i in range(len(sp)):
	res+=sp[i]//gcdd

print(res)
