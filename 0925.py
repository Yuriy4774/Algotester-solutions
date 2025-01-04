n = int(input())
sp = list(map(int,input().split()))

a = 0
for i in range(n-1,-1,-1):
    if a <= sp[i]:
        a = sp[i]
    else:
        sp.pop(i)
print(len(sp))
print(*sp)
