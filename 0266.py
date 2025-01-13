n,m = map(int,input().split())
sp = list(map(int,input().split()))

res=  0
for i in range(n):
    res+=sp[i]**2
if res % m == 0:
    print("Yes")
else:
    print("No")