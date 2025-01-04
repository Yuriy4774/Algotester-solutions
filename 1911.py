x_start, y = map(int, input().split())
x = x_start**2
x += 4
x *= 14
x /= 7
x -= 8
x *= 50
x  = round(x**0.5)
x += 47
x -= (10*x_start)

if x == y:
    print("Magic")
else:
    print("Too much juice")
