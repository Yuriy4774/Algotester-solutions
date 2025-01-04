inputs = input()
v,x,a,b = inputs.split()
v,x,a,b = int(v),int(x),int(a),int(b)
a,b = min(a,b),max(a,b)

def can(v,x,zypunka):
    tram = zypunka // v
    petro = abs(x-zypunka)
    return tram>=petro
can_first = can(v,x,a)
can_second = can(v,x,b)

if can_first and can_second:
	if abs(x - a) <= abs(x - b):
		print("1")
	else:
		print("2")
elif can_first or can_second:
	if can_first:
		print("1")
	else:
		print("2")
else:
	print("-1")
