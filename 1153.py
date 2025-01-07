n = int(input())

res,five = 0,5
while five <= n:
    res+=n//five
    five*=5
print(res)