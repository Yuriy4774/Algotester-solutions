import math
n = int(input())
res = 11
full_m = max(math.ceil(n / 60),1)
i = 0
if full_m >= 7:
    full_m -= 7
    res += 7 * 9
    res += full_m * 5
else:
    res += 9 * full_m
print(res)

