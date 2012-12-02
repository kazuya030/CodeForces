import copy
import math
import sys

def solve(LR):
    n = len(LR)
    l_LR = list(LR)

    half = n/2
    ans=[]

    if LR.count('L') > half:
        more, less = 'L', 'R'
    else:
        more, less = 'R', 'L'

    homoness = []
    for i in range(half):
        ans.append([i, i+half])

        if LR[i]==less and LR[i+half]==less:
            homoness.append('homo_less')
        elif LR[i]==less or LR[i+half]==less:
            homoness.append('hetero')
        else:
            homoness.append('homo_more')

    for i in range(half):
        if homoness[i] == 'homo_less':
            j = homoness.index('homo_more')
            if math.fabs(i-j) == 1:
                ans[i] = [i, j+half]
                ans[j] = [j, i+half]
            else:
                ans[i] = [i, j]
                ans[j] = [i+half, j+half]
            homoness[i] = homoness[j] = 'hetero'

    ans_form = []
    for i in range(half):
        if homoness[i] == 'hetero':
            if LR[ans[i][0]] == 'L':
                ans_form.append("%d %d" % (ans[i][0]+1, ans[i][1]+1) )
            else:
                ans_form.append("%d %d" % (ans[i][1]+1, ans[i][0]+1) )
        else:
            ans_form.append("%d %d" % (ans[i][0]+1, ans[i][1]+1) )

    return "\n".join(ans_form)

def check(inp):
    n = len(inp)
    for i in range(n):
        t = inp[i][0]-inp[i][1]
        if t == 1 or t == -1:
            return False
    return True

def test(LR):
    tmp = solve(LR)
    print LR
    print tmp
    print


if __name__ == '__main__':

    try:
        try:
            f_in = open(__file__[:-2]+"in")
            f_out = open(__file__[:-2]+"out", 'w')
        except IOError:
            f_in = open("input.txt")
            f_out = open("output.txt", 'w')
        FLAG_LOCAL = True

        n = int(f_in.next())
        LR = f_in.next()

        output = solve(LR)
        print output,

        if FLAG_LOCAL:
            f_out.write(output)
            f_in.close()
            f_out.close()

    except IOError:
        test('LLRLLL')
        test('LLRLLR')
        test('LRLRLR')
        test('RLLL')
        test('LLLR')
        #test('LRLR') #<- impossible
        test('RRLL')
        test('RRRR')


        #f_in = sys.stdin
        FLAG_LOCAL = False

