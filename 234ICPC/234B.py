import copy
import math
import sys

def solve(n, k, b):
    b_sorted = copy.copy(b)
    b_sorted.sort()
    th = b_sorted[-k]
    ans = [i+1 for i, v in enumerate(b) if v>= th]


    if len(ans) != k:
        times = len(ans)-k
        dup = [i+1 for i, v in enumerate(b) if v== th]
        #print times, dup, dup[0]
        for i in range(times):
            ans.remove(dup[0])
            dup.pop(0)

    return [th, " ".join(map(str, ans))]


if __name__ == '__main__':
    try:
        try:
            f_in = open(__file__[:-2]+"in")
            f_out = open(__file__[:-2]+"out", 'w')
        except IOError:
            f_in = open("input.txt")
            f_out = open("output.txt", 'w')
        FLAG_LOCAL = True
    except IOError:
        f_in = sys.stdin
        FLAG_LOCAL = False

    n, k = [int(_) for _ in f_in.next().split()]
    b = [int(_) for _ in f_in.next().split()]

    output = solve(n, k, b)
    print output[0]
    print output[-1]

    if FLAG_LOCAL:
        f_out.write(str(output[0])+'\n'+output[1])
        f_in.close()
        f_out.close()