n = int(input())
sp = []
for i in range(n*3):
    x,y = map(int,input().split())
    sp.append([x,y])
orig = sp.copy()
def compare(x):
    return x[0],x[1]

sp.sort(key = compare)
for i in range(0,len(sp),3):
    a,b,c = sp[i],sp[i+1],sp[i+2]
    a1,b1,c1 = orig.index(a)+1,orig.index(b)+1,orig.index(c)+1
    print(a1,b1,c1,sep = " ")
