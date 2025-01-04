n,x = map(int,input().split())
sp = list(map(int,input().split()))

res = x - sum(sp)
if res <= 0:
    print("Another mistake!")
else:
    print(res)
