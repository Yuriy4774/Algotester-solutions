import math

n = int(input())
sp = list(map(int,input().split()))

sp+=sp

res,a = 0,0
for i in range(len(sp)):
    if sp[i] == 0:
        a+=1
    else:
        res = max(res,a)
        a = 0

print(math.ceil(res/2))
