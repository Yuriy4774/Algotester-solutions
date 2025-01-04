n = int(input())
sp = [[] for _ in range(n)]
s = []
for i in range(n):
    a,b = input().split()
    b = int(b)
    sp[i] = [a,b]
    s.append(a)
s = list(set(s))
res = 0
for i in range(len(s)):
    el = s[i]
    res_i = 0
    for j in range(n):
        if sp[j][0] == el:
            res_i = max(res_i,sp[j][1])
    res+= res_i

print(res)
