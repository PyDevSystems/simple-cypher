# PYDEVSYSTEMS'S Simple Cypher <pydevsystems@gmail.com>
# THIS SOFTWARE IS NOT COPYRIGHTED

def crypt(t):
    t = [t[x:x + 4] for x in range(0, len(t), 4)]
    nt = []
    for x in t:
        if len(x) < 4:
            x = x + "м" * (4 - len(x))
        nt += [x, ]
    t = nt
    del nt

    e = ""
    for c in range(0, 4):
        for l in range(0, len(t)):
            e += t[l][c]

    e = ''.join([e[x:x + 4] for x in range(0, len(e), 4)][::-1])[::-1]
    a = ""
    for x in range(0, len(e)):
        try:
            a += e[::-1][x]
            a += e[1::-2][x]
            a += e[1::-4][x]
        except IndexError:
            pass

    return a


if __name__ == '__main__':
    while 1:
        print(crypt(input(">>> ")))
