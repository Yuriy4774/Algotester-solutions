n = int(input())
sp = list(map(int,input().split()))

if n >= 3:
    print("Marichka")
    print(sp[0],end = " ")
    for i in range(n-1):
        print(0,end=" ")
elif n == 2:
    if sp[0] == sp[1]:
        print("Zenyk")
    else:
        print("Marichka")
        if sp[0] > sp[1]:
            print(abs(sp[0]-sp[1]),0)
        else:
            print(0,abs(sp[0]-sp[1]))
print()
