n = int(input())
index = list(map(int, input().split()))

pos = [0] * (n + 1)
pref = [0] * (n + 1)

for i in range(n):
    pos[index[i]] = i
    
    pref[i + 1] = pref[i] + index[i]


q = int(input())
for x in range(q):
    zapyt = list(map(int, input().split()))
    if zapyt[0] == 1:
        for i in range(zapyt[1]):
            leader = pos[1]
            index[leader - 1], index[leader] = index[leader], index[leader - 1]
            pos[index[leader - 1]] = leader - 1
            pos[index[leader]] = leader
        
            pref[leader] = pref[leader - 1] + index[leader - 1]
    elif  zapyt[0] == 2:
        leader = pos[zapyt[1]]
        index[leader - 1], index[leader] = index[leader], index[leader - 1]
        pos[index[leader - 1]] = leader - 1
        pos[index[leader]] = leader

        pref[leader] = pref[leader - 1] + index[leader - 1]
    elif zapyt[0] == 3:
        l = (pos[zapyt[1]] + 1) - zapyt[2]
        r = (pos[zapyt[1]] + 1) - 1
        print(pref[r] - pref[l - 1])