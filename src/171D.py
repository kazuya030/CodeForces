import copy
import math
import sys

def solve(n):

    if n==1:
        return 2
    elif n==2:
        return 3
    elif n==3:
        return 1
    elif n==4:
        return 2
    else:
        return 1


if __name__ == '__main__':

    FLAG_LOCAL = False

    if FLAG_LOCAL:
        str_in = __file__[:-2]+"in"
        f_in = open(str_in)
        f_out = open(str_in.rstrip('.in') + '.out', 'w')
    else:
        f_in = sys.stdin

    n = int(f_in.next())
    output = str(solve(n))

    if FLAG_LOCAL:
        f_out.write(output)


    print output,
    if FLAG_LOCAL:
        f_in.close()
        f_out.close()