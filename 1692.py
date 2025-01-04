n = int(input())
sp = input()
b,a = sp.count("0"),sp.count("1")
b,a = int(b),int(a)
if a >= b:
    for i in range(a):
        print(1,end="")
else:
    for i in range(b):
        print(0,end="")

