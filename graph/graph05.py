''' Question: 순위
*   https://programmers.co.kr/learn/courses/30/lessons/49191
'''

from collections import defaultdict


def solution(n, results):

    win, lose = defaultdict(set), defaultdict(set)
    for winner, loser in results:
        win[winner].add(loser)
        lose[loser].add(winner)

    for i in range(n-1):
        for winner, loser in results:
            win[winner].update(win[loser])
            lose[loser].update(lose[winner])

    count = 0
    for player in range(1, n+1):
        if len(win[player]) + len(lose[player]) == n - 1:
            count += 1

    return count
