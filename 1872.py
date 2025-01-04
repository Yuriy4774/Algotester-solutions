n = input()
def is_lucky(n):
    for i in range(0,len(n)):
        if n[i] == '4' and i != len(n) - 1:
            if n[i+1] == '7':
                return "YES"
    return "NO"
print(is_lucky(n))
