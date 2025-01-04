a,b = map(int, input().split())
res = ""
if a < b:
    color = 'G'
else:
    color = 'Y'
for i in range(min(a,b)*2):
    res += color
    if color == 'G':
        color = 'Y'
    else:
        color = 'G'

if max(a,b) == a:
    color = 'Y'
else:
    color = 'G'
    
for j in range(max(a,b)-min(a,b)):
    res+=color

print(res)