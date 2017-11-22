# PYDEVSYSTEMS'S Simple Cypher
# THIS SOFTWARE IS NOT COPYRIGHT
#
#   Giving credit's to author is very very cool,
#   but is not mandatory.
#
# <pydevsystems@gmail.com>
# <http://github.com/pydevsys/simple-cypher>
# <http://github.com/pydevsys>
#

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
