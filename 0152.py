n, k = map(int, input().split())
sp = []
for i in range(n):
    sp.append([int(digit) for digit in input()])

r = 1
while r <= n:
    good = False
    for i in range(0, n-r + 1):
        for j in range(0, n-r + 1):
            num = 0
            
            for q in range(i, i + r):
                for l in range(j, j + r):
                    if sp[q][l] == 1:
                        num += 1
            if num <= k:
                good = True
                break
        if good:
            break

    if good:
        r += 1
    else:
        break
res = r-1
print(res)
