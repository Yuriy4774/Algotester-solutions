sp = list(map(str,input().split()))
for i in range(0,len(sp)):
    sp[i] = sp[i].lower()

print(len(set(sp)))

