''' Question: 도둑질
** https://programmers.co.kr/learn/courses/30/lessons/42897
'''


# Recursive solution
def solution1(money):

    def max_rob(begin, end, memoize):
        if begin > end:
            return 0
        if begin == end:
            return money[begin]
        if (begin, end) in memoize:
            return memoize[(begin, end)]

        result = max(max_rob(begin+1, end, memoize),
                     max_rob(begin+2, end, memoize) + money[begin])

        memoize[(begin, end)] = result
        return result

    n = len(money)
    memoize = {}
    return max(max_rob(1, n-1, memoize),
               max_rob(2, n-2, memoize) + money[0])


# Iterative solution
def solution2(money):

    n = len(money)
    if n == 3:
        return max(money)

    # When the first house is robbed
    first = rob(0, n-1, money)

    # When the first house is NOT robbed
    not_first = rob(1, n, money)

    return max(first, not_first)


def rob(begin, end, money):
    near, far, result = 0, 0, 0
    for i in range(begin, end):
        result = max(far + money[i], near)
        far = near
        near = result
    return result
