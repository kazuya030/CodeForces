#coding: utf8
import sys
import StringIO
__date__ = '2012/10/20'

from A import solve

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


if __name__ == '__main__':
    test("wjmzbmr", "CHAT WITH HER!")
    test("xiaodao", "IGNORE HIM!")
    test("sevenkplus", "CHAT WITH HER!")


