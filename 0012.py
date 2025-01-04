n = int(input())
SP = []

for i in range(n):
    sp = list(map(int, input().split()))
    SP.append(sp)

res = 0

for i in range(3):
    a = []
    for j in range(n):
    	a.append(SP[j][i])
    a.sort()
    b = a[n // 2]
    
    total_difference = 0
    for j in a:
        res+=abs(j-b)
print(res)
