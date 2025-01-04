def max_efficiency(n, sweets):
    maximum = -100000000000000000
    minimum = 10000000000000000000

    for i in range(0,n):
        value = int(sweets[i]) - i
        if value > maximum:
            maximum = value
        if value < minimum:
            minimum = value
    efficiency = maximum - minimum
    return efficiency

n = int(input())
sweets = input()
sweets = sweets.split()

print(max_efficiency(n, sweets))

