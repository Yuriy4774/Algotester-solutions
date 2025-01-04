n, m = map(int, input().split())

while n > 0 and m > 0:
    if n >= m:
        m = 0
    else:
        m -= n
    n -= 1

if m == 0 and n == 0:
    print("Best possible scenario!")
elif m == 0:
    print("BNR will finally be free!")
else:
    print("Special military operation completely failed!")
