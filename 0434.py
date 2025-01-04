a = input()
b = input()
a,b,y = sorted(a),sorted(b),True

for i in b:
    if i in a:
        a.remove(i)
    else:
        y = False
        break

if y:
    print("YES")
else:
    print("NO")

