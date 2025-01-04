n, k = map(int, input().split())
sp = list(map(int, input().split()))

sp.sort()
a,prev,m = [],sp[0],0
for i in sp:
    if i != prev:
        m = max(len(a),m)
        a = []
        prev = i
    a.append(i)
m = max(len(a),m)
if m < k:
    print("Oh sh*t")
else:
    print(*sp)

