import copy
import math
import sys

def solve(n):
    if n%2== 1:
        return -1
    else:
        ret=range(1, n+1)
        half = n/2
        for i in range(half):
            ret[i] += half
            ret[i+half] -= half
        return " ".join(map(str, ret))



if __name__ == '__main__':
    try:
        f_in = open(__file__[:-2]+"in")
        f_out = open(__file__[:-2]+"out", 'w')
        FLAG_LOCAL = True
    except IOError:
        FLAG_LOCAL = False
        f_in = sys.stdin

    n = int(f_in.next())
    output = str(solve(n))

    print output,

    if FLAG_LOCAL:
        f_out.write(output)
        f_in.close()
        f_out.close()