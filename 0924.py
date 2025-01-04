n = int(input())
sp = list(map(int, input().split()))
one,two = 0,0
res = []
if sum(sp) % 2 == 0:
    arr = []
    for i in range(0,len(sp)):
        arr.append([sp[i],i])
    arr.sort(reverse=True)
    #print(arr)
    for i in range(n):
        if one <= two:
            one+=arr[i][0]
        else:
            two+=arr[i][0]
            res.append(arr[i][1]+1)

    if one == two:
        print(len(res))
        print(*res)
    else:
        print(-1)
else:
    print(-1)

