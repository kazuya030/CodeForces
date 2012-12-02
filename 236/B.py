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
    if k<=1:
        return []
    ans = []
    for p in l_p:
        if k%p==0:
            ans.append(p)
            k/= p

            while k%p==0 :
                ans.append(p)
                k/= p

            if k==1:
                return ans
    ans.append(k)
    return ans

def count(divs):
    if len(divs)==0:
        return 1
    s = set(divs)
    ans = 1
    for i in s:
        ans *= (divs.count(i)+1)
    return ans


def readline():
    return map(int, raw_input().split())

def solve():
    l_p = primes(10)
    l_div = [div(_, l_p) for _ in range(101)]

    t = readline()
    t.sort()

    d = {}
    d_count ={}
    N = max(t)
    p_comb = itertools.combinations_with_replacement(range(1, N+1), 3)
    for a,b,c in p_comb:
        if not d.has_key(a*b*c):
            divs = l_div[a]+l_div[b]+l_div[c]
            n = count(divs)
            d[a*b*c] = n

    ans = 0
    a,b,c = t

    for i in range(1, a+1):
        for j in range(1, b+1):
            for k in range(1, c+1):
                prod = i*j*k

                ans += d[prod]

    print ans%1073741824
    return 0





if __name__ == '__main__':
    solve()
