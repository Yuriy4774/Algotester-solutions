n = int(input())
algoritmy = input()
algoritmy = list(map(int, algoritmy.split()))
counter = 1
for i in range(0,n):
    if i != n - 1:
        if algoritmy[i] != algoritmy[i+1]:
            counter +=1
    else:
        pass

print(counter)
