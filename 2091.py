n = int(input())
p = 1
k = 10**9 + 7
for i in range(n):
    if i == 0:
        p = p * 26
    else:
        p = p * 25


ost_p = p % k
print(ost_p)
