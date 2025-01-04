#a, b = map(int, input().split())
n = int(input())
k = int(input())
jumps = []
for i in range(k):
    jumps.append(int(input()))
m = int(input())
holes = []
for i in range(m):
    holes.append(int(input()))

sp = []
for i in range(0,n):
    if i not in holes:
        sp.append(float('inf'))
    else:
        sp.append(-1)
sp[0] = 0
for i in range(0,len(sp)):
    if sp[i] == float('inf') or i in holes:
        continue
    for j in jumps:
        next_pos = i + j
        if next_pos < n and next_pos not in holes:
            sp[next_pos] = min(sp[next_pos],sp[i]+1)

        
if sp[n - 1] == float('inf'):
    print(-1)
else:
    print(sp[n - 1])
