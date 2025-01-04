n = int(input())
sp = []
res = 0
for i in range(n):
    a = input()
    a = "".join(sorted(a))
    a = hash(a)
    if a not in sp:
        res+=1
        sp.append(a)
print(res)
