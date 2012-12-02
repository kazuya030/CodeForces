#coding: utf8
import sys
import time
import StringIO
__date__ = '2012/10/20'

from B import solve


def test(input, ans):
    ans = str(ans)

    s_in = StringIO.StringIO(input)
    s_out = StringIO.StringIO()
    sys.stdin = s_in; sys.stdout = s_out
    str(solve())
    sys.stdin = sys.__stdin__; sys.stdout = sys.__stdout__

    ans_tmp = s_out.getvalue().strip()

    if ans_tmp == ans:
        print "Correct %s -> %s" % (repr(input), repr(ans))
    else:
        print "Wrong!! %s should %s not %s" % (repr(input), repr(ans), repr(ans_tmp))

def calcDuration(args, fn=test):
    s = time.clock()
    fn(*args)
    print 'Duration = %f[ms]' % ((time.clock()-s)*1000)

if __name__ == '__main__':
    #test("2 2 2", 20)
    test("5 6 7", 1520)
    test("5 5 5", 728)
    calcDuration(["100 100 100", 0])
    #test("1 1 1", 1)
    #test("1 1 2", 3)
    #test("2 1 1", 3)




