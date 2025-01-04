def main():
	n, m = map(int, input().split())
	t = m % 2 == 1
	if t:
		n, m = m, n
	if m % 2 == 1:
		print("-1")
		return
	ans = []
	c = ord('A')
	for i in range(n):
		ans.append([])
		for j in range(m):
			ans[i].append(chr(c))
			c += j % 2
	if t:
		n, m = m, n
	for i in range(n):
		for j in range(m):
			print(ans[j][i] if t else ans[i][j], end='')
		print()

main()