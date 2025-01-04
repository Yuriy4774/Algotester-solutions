n, k = map(int, input().split())

sp = list(range(1, n + 1))

a = n-k+1
b = sp[:a]
sp = b[::-1] + sp[a:]
print(*sp)

