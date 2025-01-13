n = input()
def deff(n):
    if len(n) % 2 == 0:
        centre = len(n) // 2
        a,b = n[:centre],n[centre:]
        if a != b[::-1]:
            return len(n)
    else:
        centre = len(n) // 2
        a,b = n[:centre],n[centre+1:]
        if a != b[::-1]:
            return len(n)
    if n.count(n[0]) == len(n):
        return -1
    else:
        return len(n) -1
print(deff(n))