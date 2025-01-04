n = int(input())
a = list(map(int, input(). split()))

sp = {key: 0 for key in a}
for i in a:
    sp[i] += 1
    
print(n - max(sp.values()))
