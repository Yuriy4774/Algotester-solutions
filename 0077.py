l,r = 1,10**9
while l <= r:
    mid = (l+r) // 2
    print(mid,flush=True)
    s = input().strip()
    if s == '<':
        l = mid+1
    elif s == '>':
        r = mid-1
    else:
        exit()

