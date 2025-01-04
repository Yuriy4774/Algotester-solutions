n = input()
a = n[0]
res = 1
for i in range(0,len(n)):
    if n[i] != a:
        a = n[i]
        res += 1
print(res)

