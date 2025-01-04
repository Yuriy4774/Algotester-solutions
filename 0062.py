n,m = map(int,input().split())
sp = []
for i in range(n):
    a,b = map(int,input().split())
    sp.append((a,b))

gr = []
for i in range(n):
    gr.append([])

for _ in range(m):
    a, b = map(int, input().split())
    gr[a - 1].append(b - 1)
    gr[b - 1].append(a - 1)

#----------
def bfs(start, visited):
    q = [start]
    visited[start] = True
    sp1 = []
    
    while len(q) > 0:
        x = q.pop(0)
        sp1.append(x)
        for neight in gr[x]:
            if not visited[neight]:
                visited[neight] = True
                q.append(neight)
    
    return sp1

visited = [False] * n
res = 0

for i in range(n):
    if visited[i] == False:
        gr_part = bfs(i,visited)
        summa_a,summa_b=  0,0

        for j in gr_part:
            summa_a += sp[j][0]
            summa_b += sp[j][1]
        if summa_a > summa_b:
            res += summa_a - summa_b
print(res)