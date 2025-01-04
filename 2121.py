n = int(input())
sp = list(map(int,input().split()))
max_sum = 0
while len(sp) != 0:
    a, b = min(sp), max(sp)
    max_sum = max(max_sum, a + b)
    sp.remove(a)
    sp.remove(b)


print(max_sum)
