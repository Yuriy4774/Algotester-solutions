n = int(input())
sp = list(input())
a = "abcdefghijklmnopqrstuvwxyz"
for i in range(0,len(sp),2):
    first = sp[i]
    second = sp[i+1]
    for j in a:
        if j == first:
            sp[i+1] = first
            sp[i] = second
        elif j == second:
            sp[i] = first
            sp[i+1] = second

for k in sp:
    print(k,end="")
