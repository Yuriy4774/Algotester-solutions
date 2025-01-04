n = int(input())
sp = list(map(int,input().split()))
q = int(input())

SP = [0]
for i in range(1,n + 1):
	if i % 2 == 0:	
		SP.append(sp[i - 1] + SP[i - 1])
	else:
		SP.append(SP[i - 1]- sp[i - 1])


for i in range(q):
    l, r = map(int, input().split())
    a = SP[r] - SP[l - 1]
    if l % 2 != r % 2:
        a = 0
    elif l % 2 == 1:
        a = -1*a
    print(2*a)


