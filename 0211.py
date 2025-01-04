n,m = map(int, input().split())
n_s,m_s = set(),set()
for i in range(n):
    a = input()
    n_s.add(a)

for i in range(m):
    a = input()
    m_s.add(a)
print(len(n_s.union(m_s)))

