import copy
import math
import sys

def solve(top, dices):
    def getID(n):
        return math.fabs(2*n-7)

    N = len(dices)

    stock = set([1, 3, 5])

    stock.remove(getID(top))

    for i in range(N):
        b = set([getID(dices[i][0]), getID(dices[i][1])])
        if stock != b:
            return "NO"


    return "YES"


if __name__ == '__main__':

    FLAG_LOCAL = True

    if FLAG_LOCAL:
        str_in = __file__[:-2]+"in"
        f_in = open(str_in)
        f_out = open(str_in.rstrip('.in') + '.out', 'w')
    else:
        f_in = sys.stdin

    N = int(f_in.next())
    top = int(f_in.next())
    dices = list()

    for num_q in range(N):
        L,R = [int(_) for _ in f_in.next().split()]
        dices.append([L, R])

    output = solve(top, dices)
    if FLAG_LOCAL:
        f_out.write(output)


    print output,
    if FLAG_LOCAL:
        f_in.close()
        f_out.close()