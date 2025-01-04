n, w = map(int, input().split())

for i in range(n):
     s = list(map(int, input().split()))
     for j in range(s[0]):
          w += s[j+1]
     print(w)

