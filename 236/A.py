#coding: utf8
import math
import copy
import sys


def readline():
    return map(int, raw_input().split())

def solve():
    name = len(set(raw_input()))
    if name%2 != 0:
        print "IGNORE HIM!"
    else:
        print "CHAT WITH HER!"



if __name__ == '__main__':
    solve()
