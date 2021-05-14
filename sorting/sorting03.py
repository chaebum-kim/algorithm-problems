''' Question: H-Index
*   https://programmers.co.kr/learn/courses/30/lessons/42747#
'''


def solution(citations):

    citations.sort()
    n = len(citations)
    for i in range(n):
        if citations[i] >= n - i:
            return n - i
    return 0
