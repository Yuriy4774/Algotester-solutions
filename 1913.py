n = int(input())
a = list(map(int, input().split()))

q = int(input())
for _ in range(q):
    x,y = map(int, input().split())
    result = 0
    for i in range(x-1,y):
        suma = 0
        for j in range(i,y):
            suma += a[j]
            if suma == 0:
                result += 1
    print(result)
