n = int(input())
c = input()
sp = []
for i in range(n):
    sp.append(input())

def bs(s,c):
    p = len(s)
    for i in range(len(s)):
        if s[i] > c:
            p = i
            break
    s = s[:p] + c + s[p:]

    return s

sp_s = []
for i in range(n):
    sp_s.append(bs(sp[i],c))

print(min(sp_s))
