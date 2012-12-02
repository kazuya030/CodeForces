import copy
import math
import sys

def primes(n):
    if n==2: return [2]
    elif n<2: return []
    s=range(3,n+1,2)
    mroot = n ** 0.5
    half=(n+1)/2-1
    i=0
    m=3
    while m <= mroot:
        if s[i]:
            j=(m*m-3)/2
            s[j]=0
            while j<half:
                s[j]=0
                j+=m
        i=i+1
        m=2*i+3
    return [2]+[x for x in s if x]

def divisors(n):
    sqrt = int(math.sqrt(n))
    l_facs = primes(10**6)
    ans = []
    for p in l_facs:
        if n % p == 0:
            ans.append(p)
            n /= p
            while n%p==0:
                ans.append(p)
                n /= p

        if p>sqrt:
            break
    return ans

def solve(n):
    l_facs = primes(10**6)
    l_divs = []
    n_temp = n
    for p in l_facs:
        if n_temp%p == 0:
            l_divs.append(p)
            n_temp %= p

            #####while()


    return -1


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