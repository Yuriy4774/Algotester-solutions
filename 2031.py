n = int(input())
for i in range(4):
    if (n - i*7) % 4 == 0 and n-i*7 >= 0:
        print("Yes")
        exit()
print("No")
