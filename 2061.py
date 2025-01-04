import math
sp = list(map(int,input().split()))
n,k,c=sp[0],sp[1],sp[2]
potribno = n *4
print(math.ceil((n*4)/k)*c)

