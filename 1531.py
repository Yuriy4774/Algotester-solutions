n = int(input())

sp = list(map(int, input().split()))
sp1 = list(map(int, input().split()))
if sp[::-1] == sp1:
    print("Yes")
else:
    print("No")
    print(*sp[::-1])
