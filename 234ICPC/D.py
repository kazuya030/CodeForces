#coding: utf8
import math
import copy
import sys

def printe(inp):
    sys.stderr.write(repr(inp)+'\n')
    #sys.stderr.flush()

def readline():
    return map(int, raw_input().split())

def solve():
    m, k = readline()
    favorite = set(readline())
    n = int(raw_input())
    l_name = []
    n_actors = []
    ind_actors = []
    min_fav_actors = []
    max_fav_actors = []
    for i in range(n):
        l_name = raw_input()
        n_actors = int(raw_input())
        ind_actors = readline()
        num_zero = ind_actors.count(0)

        min_fav_actors = len(favorite & set(ind_actors))
        max_fav_actors = min_fav_actors + ind_actors.count(0)

        printe([min_fav_actors, max_fav_actors])





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
