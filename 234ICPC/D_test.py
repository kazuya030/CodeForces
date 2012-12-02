#coding: utf8
import sys
import StringIO
__date__ = '2012/10/20'

from D import solve

def test(input, ans):
    ans = str(ans)

    s_in = StringIO.StringIO(input)
    s_out = StringIO.StringIO()
    sys.stdin = s_in; sys.stdout = s_out
    str(solve())
    sys.stdin = sys.__stdin__; sys.stdout = sys.__stdout__

    sys.stdout.flush()
    ans_tmp = s_out.getvalue()

    if ans_tmp == ans:
        print "Correct"
        print repr(input)
        print ans
        print
    else:
        print "Wrong!!! :", repr(input)
        print "TrueAnswer"
        print ans
        print "YourAnswer"
        print ans_tmp


if __name__ == '__main__':
    test("""5 3
1 2 3
6
firstfilm
3
0 0 0
secondfilm
4
0 0 4 5
thirdfilm
1
2
fourthfilm
1
5
fifthfilm
1
4
sixthfilm
2
1 0
"""
,"""2
2
1
1
1
2
""")


