n = int(input())
sp = list(map(int,input().split()))
sp.sort()
res = sp[-1] - sp[0]
print(res)
