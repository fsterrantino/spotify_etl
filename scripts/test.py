def modification(n):
    n = n + 1
    return n

def original():
    n = 0
    n = modification(n)
    print(n)

original()