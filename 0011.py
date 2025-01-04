n = int(input())
sp = list(map(int,input().split()))
res = 0
for i in sp:
    res += i - 1

print(res)
