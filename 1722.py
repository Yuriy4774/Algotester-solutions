n,m = map(int,input().split())
sp = list(map(str,input().split()))
abc = list(map(int,input().split()))
#print(sp)
sp_c = []
d = dict()
for i in range(m):
    d[chr(97+i)] = 0
#print(d)
for i in range(n):
    
    for j in range(len(sp[i])):
        d[sp[i][j]]+=1

for i in range(m):
    d[chr(97+i)] = d[chr(97+i)] - abc[i]
a = ""
for i in range(m):
    for j in range(d[chr(97+i)]):
        a+=chr(97+i)
#print(a,d)
r = False
for i in range(n):
    #print(sorted(sp[i]))
    if "".join(sorted(sp[i])) == a and len("".join(sorted(sp[i]))) == len(a):
        if r != False:
            print("Someone call SCP Foundation")
            exit()
        r = sp[i]
print(r)