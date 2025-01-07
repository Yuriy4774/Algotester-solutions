n = int(input())
sp = []
for i in range(n):
    sp.append(input())

a = input()
for i in range(n):
    if a == sp[i][4:]:
        sp[i] = sp[i][:1] + "/" + sp[i][2:]
    
for i in range(n):
    print(sp[i])