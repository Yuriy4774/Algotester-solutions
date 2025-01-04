n = input()
sp = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
sp1 = list("0123456789")
sp2 = list("!@#$%&*()_-+=[]{};:/?.>,<~")
if n.capitalize() in sp:
    print(sp.index(n.capitalize())+1)
elif n in sp1:
    print("digit")
elif n in sp2:
    print("weird symbol")
