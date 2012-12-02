#coding: utf8
import math
import copy
import sys

__date__ = '2012/10/20'

def readline():
    return map(int, raw_input().split())

def solve():
    N = int(raw_input())
    input = raw_input()
    half = N/2
    for i in xrange(half):
        if input[i] == 'R':
            print "%d %d" % (i+half+1, i+1)
        else:
            print "%d %d" % (i+1, i+half+1)


if __name__ == '__main__':
    try:
        f_in = open("input.txt")
        f_out = open("output.txt", 'w')
        FLAG_FILE = True
    except IOError:
        FLAG_FILE = False
    else:
        sys.stdin = f_in
        sys.stdout = f_out

    solve()

    if FLAG_FILE:
        f_in.close()
        f_out.close()
