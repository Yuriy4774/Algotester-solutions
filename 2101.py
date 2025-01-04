a,b,c = list(map(int,input().split()))
if b >= a +c:
    print("All")
elif b >= a:
    print("All registered")
else:
    print("Bad organizers")
