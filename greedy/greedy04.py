''' Question: 구명보트
*   https://programmers.co.kr/learn/courses/30/lessons/42885
'''


def solution(people, limit):

    people.sort()
    n = len(people)
    left, right = 0, n-1
    group = 0

    while left < right:
        if people[left] + people[right] <= limit:
            group += 1
            left += 1
        right -= 1

    return n - group
