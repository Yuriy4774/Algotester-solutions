n = int(input())
sp = []
for i in range(n):
    a = input()
    sp.append(a)

a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def check(s):
    surname,name = "",""
    yes = False
    for i in s:
      if i in a:
            yes = not yes
      if yes:
            surname+=i
      else:
            name+=i
    ans = name+ surname
    return ans
for i in sp:
     print(check(i))
      
