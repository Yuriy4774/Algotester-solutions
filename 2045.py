#m, n = map(int, input().split())
n = int(input())
input_arr = list(input().split())
sp = []
for i in range(8):
    a = []
    for j in range(8):
        a.append('.')
    sp.append(a)

def to_num(string):
    dictonary = {
        'a': 1,
        'b': 2,
        'c' : 3,
        'd' : 4,
        'e' : 5,
        'f' : 6,
        'g' : 7,
        'h' : 8
        }
    return dictonary.get(string, 0) 
horses = []
for i in input_arr:
    x,y = i[0],int(i[1])-1
    x = to_num(x)
    #sp[7-y][x-1] = 'K'
    horses.append([7-y,x-1])

knight_moves = [
    (-2, -1), (-2, 1), (-1, -2), (-1, 2),
    (1, -2), (1, 2), (2, -1), (2, 1)
]

def is_valid(x, y):
    return 0 <= x < 8 and 0 <= y < 8

for i in horses:
    a,b = i[0],i[1]
    for move in knight_moves:
        new_a, new_b = a + move[0], b + move[1]
        if is_valid(new_a, new_b) and sp[new_a][new_b] == '.':
            sp[new_a][new_b] = 'K'

for i in sp:
    for j in i:
        print(j,end = "")
    print()
