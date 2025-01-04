n = int(input())
res = 0
for i in range(n):
    x1,y1,x2,y2 = map(int,input().split())
    res += ((x2-x1)**2+(y2-y1)**2)**0.5
print(int(res))

