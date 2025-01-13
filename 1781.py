n = input()
res = ""
for i in range(len(n)):
    if n[i] == '4' or n[i] == '7':
        res+=n[i]

if len(res) == 0:
    print("No luck")
    exit()
print(res)