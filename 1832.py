n = int(input()) 
sp_a = list(map(int, input().split()))
sp_b = list(map(int, input().split()))

sp = sorted(zip(sp_a, sp_b), reverse=True)

res = 0
current_radius = float('inf')

for a,b in sp:
    if a < current_radius: 
        res += b
        current_radius = a

print(res)
