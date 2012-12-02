import copy
import math
import sys

def solve(a, b):
    list_b=list(b)
    list_b.reverse()
    b_rev="".join(list_b)
    return str(int(a)+int(b_rev))

    #hirosegolf  さんのコード
    #return str(int(a)+int(b[::-1]))

if __name__ == '__main__':

    FLAG_LOCAL = True

    if FLAG_LOCAL:
        str_in = __file__[:-2]+"in"
        f_in = open(str_in)
        f_out = open(str_in.rstrip('.in') + '.out', 'w')
    else:
        f_in = sys.stdin

    a,b = f_in.next().split()
    output = solve(a,b)

    if FLAG_LOCAL:
        f_out.write(output)


    print output,
    if FLAG_LOCAL:
        f_in.close()
        f_out.close()