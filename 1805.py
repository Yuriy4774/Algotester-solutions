n=int(input())
sp = list(map(int,input().split()))
if sum(sp) % 2 == 0:
    print("Zenyk")
else:
    print("Marichka")
