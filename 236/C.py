#coding: utf8
import math
import copy
import sys
import itertools

def printe(inp):
    sys.stderr.write(repr(inp)+'\n')
    #sys.stderr.flush()

def primes(n):
    """http://code.activestate.com/recipes/366178-a-fast-prime-number-list-generator/"""
    if n==2: return [2]
    elif n<2: return []
    s=range(3,n+1,2)
    mroot = n ** 0.5
    i_half=(n+1)/2-1
    i=0
    m=3
    while m <= mroot:
        if s[i]:
            j=(m*m-3)/2
            s[j]=0
            while j<i_half:
                s[j]=0
                j+=m
        i=i+1
        m=2*i+3
    return [2]+[x for x in s if x]

def div(k, l_p):
    if k==1:
        return set()
    ans = set()
    for p in l_p:
        if k%p==0:
            ans.add(p)
            k/= p

            while k%p==0 :
                k/= p

            if k==1:
                return ans
    return ans


def readline():
    return map(int, raw_input().split())

def solve():
    n = int(raw_input())
    l_p = primes(int(math.sqrt(n+1)+1))
    nset = set()

    if n==1:
        print 1
        return
    elif n==2:
        print 2
        return

    cand = [n, n-1]
    next = n-2
    d = {}
    for i in cand:
        d[i] = div(i, l_p)

    ans = []
    Flag_Repeat = True
    while Flag_Repeat:
        cand.append(next)
        d[next] = div(next, l_p)
        next -= 1

        iter = itertools.combinations(cand,3)
        for i,j,k in iter:
            #printe([d[i], d[j], d[k], d[i]&d[j]==nset and d[j]&d[k]==nset and d[i]&d[k]==nset])
            if d[i]&d[j]==nset and d[j]&d[k]==nset and d[i]&d[k]==nset:
                Flag_Repeat = False
                ans.append(i*j*k)
                #printe([i, j, k, i*j*k])


        #printe([cand, next])

    print max(ans)





if __name__ == '__main__':
    solve()
