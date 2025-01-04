import heapq

n = int(input())
sp = list(map(int, input().split()))

heapq.heapify(sp)

for i in range(n-1):
    a = heapq.heappop(sp)
    b = heapq.heappop(sp)
    s = (a + b) / 2
    heapq.heappush(sp, s)

print(*sp)

