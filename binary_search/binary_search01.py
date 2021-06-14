''' Question: 입국심사
*   https://programmers.co.kr/learn/courses/30/lessons/43238
'''


def solution(n, times):

    left = 0
    right = max(times) * (n // len(times))

    while left < right:
        middle = int((left + right) / 2)
        people = max_people(times, middle)
        if people < n:
            left = middle + 1
        else:
            right = middle

    return left


def max_people(times, target):
    count = 0
    for time in times:
        count += (target // time)
    return count
