# PYDEVSYSTEMS'S Simple Cypher <pydevsystems@gmail.com>
# THIS SOFTWARE IS NOT COPYRIGHTED

def crypt(s):
    pos, blocks = 0, []
    for x in range(0, len(s), 2):
        x = s[x:x+2]
        blocks += [x]
    blocks = blocks[::-1]
    blocks += blocks[1::-1]
    blocks = blocks[:-1]
    enc = ""
    for x in blocks:
        enc += x
    enc = enc[:-2]
    return enc

if __name__ == "__main__":
    while 1:
        print(crypt(input(">>> ")))
