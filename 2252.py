n = input()
res = []

for i in range(len(n)):
    if n[i] == 'W':
        left, rigth = 1001, 1001

        for j in range(i + 1, len(n)):
            if n[j] == 'C':
                rigth = j - i
                break

        for j in range(i - 1, -1, -1):
            if n[j] == 'C':
                left = i - j
                break

        res.append(min(left,rigth))

print(*res)

