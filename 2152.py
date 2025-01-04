import math
a,b,c = map(int, input().split())

s = a*100 + b*200 + c*400
if (math.isqrt(s))**2 == s:
    side = math.isqrt(s)
    if math.ceil(math.sqrt(a)) * 10 > side or math.ceil(math.sqrt(b)) * 10 > side or math.ceil(math.sqrt(c)) * 20 > side:
        print("No")
    else:
        print("Yes")
else:
    print("No")
