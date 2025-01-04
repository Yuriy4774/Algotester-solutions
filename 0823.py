from collections import deque

n, m, k = map(int, input().split())
sp = [list(map(int, input().split())) for _ in range(n)]

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

q = deque()
for i in range(n):
    for j in range(m):
        if sp[i][j] == 1:
            q.append((i, j))

for p in range(k):
    size = len(q)
    visited = set(q)
    
    for l in range(size):
        i, j = q.popleft()
        
        for dir_x, dir_y in dirs:
            new_i, new_j = i + dir_x, j + dir_y
            
            if 0 <= new_i < n and 0 <= new_j < m and sp[new_i][new_j] == 0 and (new_i, new_j) not in visited:
                sp[new_i][new_j] = 1
                q.append((new_i, new_j))
                visited.add((new_i, new_j))

res = sum(sum(row) for row in sp)
print(res)
