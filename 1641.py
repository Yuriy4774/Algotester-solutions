n,k = map(int,input().split())
if k % 3 != 0 or k // 3+1 > n:
    print(-1)
    exit()
count = k // 3
res = ""

for i in range(count+1):
    if i % 2 == 0:
        res+="7"
    else:
        res+="4"

for i in range((n-(count+1))):
    res = "7" + res
print(res)