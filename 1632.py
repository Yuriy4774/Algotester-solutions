n = int(input())
sp = list(map(int, input().split()))
if sp == sorted(sp) or sp == sorted(sp, reverse=True):
    print("YES")
else:
    print("NO")
