import math

a,b,c = map(int, input().split())
def lcm(x, y):
    return (x * y) // math.gcd(x, y)
ab = lcm(a,b)
abc = lcm(ab,c)
print(abc)
