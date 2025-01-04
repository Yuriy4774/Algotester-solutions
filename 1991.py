n = input()
a = int(n)


while True:

    if all(digit in '47' for digit in str(a)):
        break
    a += 1

print(a - int(n))
