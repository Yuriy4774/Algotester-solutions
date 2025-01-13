def dfs(v, sp, visited):
    visited[v] = True
    for neighbor in sp[v]:
        if not visited[neighbor]:
            dfs(neighbor, sp, visited)

n, m = map(int, input().split())
sp = [[] for _ in range(n + 1)]
gr = []

for _ in range(m):
    a, b = map(int, input().split())
    sp[a].append(b)
    sp[b].append(a)
    gr.append((a, b))

res = 0
for a, b in gr:
    sp_copy = [list(neighbors) for neighbors in sp]
    
    sp_copy[a].remove(b)
    sp_copy[b].remove(a)
    
    visited = [False] * (n + 1)
    dfs(1, sp_copy, visited)
    
    if not all(visited[1:]):
        res += 1

print(res)
