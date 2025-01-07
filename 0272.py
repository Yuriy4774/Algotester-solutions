n = int(input())
if n % 2 == 0:
    print(n//2)
else:
    if n < 9:
        print(1)
    elif n == 9:
        print(3)
    else:
        print((n-9)//2 + 2)