#!/usr/bin/python
# coding: utf8

import math
import time
import timeit
import cProfile
import doctest
import random
import bisect
clock_start = time.clock()


if 0:#__name__ == '__main__':
    doctest.testfile('test_commonlib.txt')
    #doctest.testfile('test_commonlib2.txt')


if 0: #__name__ == '__main__':
    print timeit.Timer('n in l', 'import bisect; l = range(10 ** 6);n = 555429;s=set(l)').timeit(10 ** 3)
    print timeit.Timer('n == l[bisect.bisect_left(l, n)]', 'import bisect; l = range(10 ** 6);n = 555429;s=set(l)').timeit(10 ** 6)
    print timeit.Timer('n in s', 'import bisect; l = range(10 ** 6);n = 555429;s=set(l)').timeit(10 ** 6)

    exit()

    l = range(10 ** 6);n = 10 ** 6 + 53429
    st = 'set(l)'
    print 'Profile: %s' % st; cProfile.run(st)
    st = '[_ for _ in l if _ < 1000]'
    print 'Profile: %s' % st; cProfile.run(st)
    st = '-1 in l'
    print 'Profile: %s' % st; cProfile.run(st)


    st = 'n == l[bisect.bisect_left(l, n)]'
    print 'Profile: %s' % st; cProfile.run(st)
    print timeit.Timer('n == l[bisect.bisect_left(l, n)]', 'l = range(10 ** 6);n = 10 ** 6 + 53429;s=set(l)').timeit(1000)


    random.shuffle(l)
    print 'shuffle!!!'

    st = 'set(l)'
    print 'Profile: %s' % st; cProfile.run(st)
    st = '[_ for _ in l if _ < 1000]'
    print 'Profile: %s' % st; cProfile.run(st)
    st = '-1 in l'
    print 'Profile: %s' % st; cProfile.run(st)

    s = set(l)

    st = 'list(s)'
    print 'Profile: %s' % st; cProfile.run(st)
    st = 'sorted(s)'
    print 'Profile: %s' % st; cProfile.run(st)
    st = '[_ for _ in s if _ < 1000]'
    print 'Profile: %s' % st; cProfile.run(st)
    st = '-1 in s'
    print 'Profile: %s' % st; cProfile.run(st)
    st = 'n in s'
    print 'Profile: %s' % st; cProfile.run(st)




def bench_loop():
    n = 10 ** 6 * 5
    l = range(n)
    s = set(l)
    def loop(it):
        for x in it:
            x += 1

    cProfile.run('loop(l)')
    cProfile.run('loop(s)')

def bench_append():
    l = []
    s = set([])
    n = 10 ** 6
    def appendlist():
        for i in xrange(n):
            l.append(i)
    def appendset():
        for i in xrange(n):
            s.add(i)

    cProfile.run('appendlist()')
    cProfile.run('appendset()')

def bench_minmax():
    n = 10 ** 7
    l = range(n)
    s = set(l)


    cProfile.run('max(l)')
    cProfile.run('min(l)')
    cProfile.run('max(s)')
    cProfile.run('max(s)')

def is_consective(l):
    for i in range(len(l) - 1):
        if l[i + 1] != l[i] + 1:
            return False
    return True

def product(l):
    return reduce(lambda x, y: x * y, l)

def getpermutations(s, n, ans=[], tmp=[], flag_call=True):
    """
    getpermutations(set, n) -> set の中から n 個の順列を返す
    Return the permutations of n elements from set
    """
    if flag_call:
        ans = []
    if n == 0:
        ans.append(tmp)
    else:
        for i in s:
            _s = s.copy(); _s.remove(i)
            tmp2 = tmp[:]
            tmp2.append(i)
            getpermutations(_s, n - 1, ans, tmp2, False)
    if flag_call:
        return ans

def iter_permutation(n, k):
    ans = [0] * k
    num = 1
    for i in range(n - k + 1, n + 1):
        num *= i

    for i in range(num):
        for j in range(k - 1):
            if ans[-(j + 1)] > n - k + j:
                ans[-(j + 1)] = 0
                ans[-(j + 2)] += 1
        yield ans
        ans[-1] += 1

def getvalue_permutation(l, perm):
    N = len(perm)
    ans = [0] * N
    cp_l = l[:]
    for i in range(N):
        ans[i] = cp_l[perm[i]]
        del cp_l[perm[i]]
    return ans

def getfactors(n, a):
    """getfactors(n, return []) -> n を素因数分解"""
    if n == 1:
        return a
    else:
        for i in xrange(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                a.append(i)
                return getfactors(n / i, a)
    a.append(n)
    return a


def getdivisors(n):
    """getdivisors(n) -> n の約数を求める"""

    import copy
    facs = getfactors(n, [])

    ans = [1]
    f_pre = 0
    for f in facs:
        if f_pre != f:
            f_pre = f
            c = facs.count(f)
            ans_copy = copy.copy(ans)
            for i in range(1, c + 1):
                ans += [x * (f ** i) for x in ans_copy]

    ans.sort()

    return ans

def _getprimes_naive(num):
    ans = [2]
    for i in xrange(3, num, 2):
        for p in ans:
            if i % p == 0:
                break
        else:
            ans.append(i)
    return ans

def _getprimes_sqrt(num):
    ans = [2]
    for i in xrange(3, num, 2):
        sqrt_i = int(math.sqrt(i) + 1)
        primes = [x for x in ans if x < sqrt_i]
        for p in primes:
            if i % p == 0:
                break
        else:
            ans.append(i)
    return ans

def getprimes_old(num):
    """getprimes(num) -> num までの素数を求める"""
    __N_NAIVE = 100
    if (num < __N_NAIVE):
        return _getprimes_naive(num)
    else:
        sqrt_num = int(math.sqrt(num) / 2) * 2 + 3
        ans = getprimes_old(sqrt_num)
        div = ans[:]
        for i in xrange(sqrt_num, num, 2):
            for d in div:
                if i % d == 0:
                    break
            else:
                ans.append(i)
    return ans

def getprimes_self(N):
    """getprimes(num) -> エラトステネスのふるい"""

    #TODO: N_MEMORY depends on memory size
    N_MEMORY = 10 ** 8
    n_try = (N - 1) / N_MEMORY + 1
    n_range = [ [_ * N_MEMORY, (_ + 1) * N_MEMORY] for _ in range(n_try)]
    n_range[-1] = [(n_try - 1) * N_MEMORY, N]
    n_range[0][0] = 2

    s = set([])
    for start, end in n_range:
        s |= set(range(start, end + 1))
        #print "s initialized! s=", s
        sq = int(math.sqrt(end + 1))
        for i in range(2, sq + 1):
            if i in s:
                s -= set([_x * i for _x in range(2, end // i + 1)])
                #print "s=", s
    return s


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




def getprimes(N):
    """http://code.activestate.com/recipes/366178-a-fast-prime-number-list-generator/"""
    if N==2: return [2]
    elif N<2: return []

    N_MEMORY=10
    n_try = (N-1) / N_MEMORY +1
    n_range = [ [_ * N_MEMORY, (_ + 1) * N_MEMORY] for _ in range(n_try)]
    n_range[-1] = [(n_try - 1) * N_MEMORY, N]
    n_range[0][0] = 3

    ans = []
    for start, end in n_range:
        if start %2 == 0:
            start += 1
        mroot = end ** 0.5
        i_half=(end-start+1)/2-1
        i=0
        m=start
        s = range(start, end+1, 2)
        while m <= mroot:
            if s[i]:
                j=s.index(s[i]**2)
                s[j]=0
                while j<i_half:
                    s[j]=0
                    j+=m
            i=i+1
            m=2*i+start
        ans += [x for x in s if x]
    return ans


for n in range(1, 6):
    N=10**n
    l_p = primes(N)
    print N, len([x for x in l_p if x>0.9*N])*10/float(N)


def getprimes_list(num):
    ans = getprimes(num)
    return sorted(list(ans))






#if __name__ == '__main__':
#    cProfile.run('getprimes(10**7)')





#a = len(getprimes(10 ** 7))
#print time.clock() - clock_start, a

#cProfile.run("print len(getprimes(10 ** 7))")


def isprime_old(n, l_ps):
    if n <= l_ps[-1]:
        return n == l_ps[bisect.bisect_left(l_ps, n)]
        #return n in l_ps[:i_b]
    else:
        r_n = math.sqrt(n) + 1
        if r_n > l_ps[-1]:
            raise "Prime List is not Enough"
        i_b = bisect.bisect(l_ps, r_n)
        for p in l_ps[:i_b]:
            if n % p == 0:
                #counter_prime[i] += 1
                return False
        else:
            return True

def isprime(n, l_primes = None, set_primes = None):
    import bisect
    if set_primes == None:
        set_primes = getprimes(int(math.sqrt(n))+1)

    if l_primes == None:
        l_primes = sorted(list(set_primes))


    if n <= l_primes[-1]:
        return n in set_primes
        #return n in l_ps[:i_b]
    else:
        
        r_n = math.sqrt(n)+1

        """
        ###  THIS IS WRONG
        ###  sqrt(110) = 10.48... l_primes[-1] = 7
        if r_n > l_primes[-1]:
            print r_n, l_primes[-1]
            raise "Prime List is not Enough"
        """
        i_b = bisect.bisect(l_primes, r_n)
        for p in l_primes[:i_b]:
            if n % p == 0:
                #counter_prime[i] += 1
                return False
        else:
            return True

#if __name__ == '__main__':
#    primes = sorted(list(getprimes(10 ** 6)))
#    cProfile.run("for i in range(10**4): isprime_old(109673, primes)")


def isprime_naive(num):
    sqrt_num = int(math.sqrt(num)) + 1
    primes = getprimes_old(sqrt_num)
    return isprime_old(num, primes)


def getgcm(a, b):
    """getgcm(a,b) -> a と b の最大公約数を互除法で求める。"""
    if b > a: a, b = b, a
    return b if a % b == 0 else getgcm(b, a % b)

def factorial(n):
    """factorial(n) -> n!"""
    return 1 if n <= 1 else n * factorial(n - 1)

def circulate(s):
    """circulated string"""
    l = list(s)
    l.append(l.pop(0))
    return ''.join(l)

def itob(n):
    """transform from int to binary strings"""
    ans = ''
    while n > 0:
        ans = str(n % 2) + ans
        n /= 2
    return ans
def btoi(s):
    """transform from binary strings to int"""
    ans = 0
    digs = len(s) - 1
    for (i, c) in enumerate(s):
        ans += 2 ** (digs - i) * int(c)
    return ans

