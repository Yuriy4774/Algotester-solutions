n = int(input())

a = [0] * 3
v = [[-1e9, 1e9] for i in range(3)]
for j in range(3):
    a[j] = list(map(int, input().split()))
    for i in range(n):
        if a[j][i] <= 0:
            v[j][0] = max(v[j][0], a[j][i])
        else:
            v[j][1] = min(v[j][1], a[j][i])

d = list(map(int, input().split()))

vidstan = 2e9
for D in d:
    vidstan = min(vidstan,abs(D)*2)

for x in v[0]:
    for y in v[1]:
        for z in v[2]:
            c = max(x,y,z,0)
            b = min(x,y,z,0)
            vidstan = min(vidstan,(abs(b) + abs(c))*2)
    
print(vidstan)