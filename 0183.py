x,y = map(int,input().split())
n,k = map(int,input().split())
sp = []
for i in range(n):
    xi,yi = map(int,input().split())
    sp.append(((x - xi)**2 + (y - yi)**2) ** 0.5)
sp.sort()
print(sp[k-1])