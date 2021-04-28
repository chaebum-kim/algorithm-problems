''' Question: 기능개발
*   https://programmers.co.kr/learn/courses/30/lessons/42586
'''

from collections import deque
import math


def solution(progresses, speeds):

    days = deque()
    for i, p in enumerate(progresses):
        days.append(math.ceil((100-p)/speeds[i]))

    answer = []
    while days:
        day = days.popleft()
        count = 1
        while days and day >= days[0]:
            count += 1
            days.popleft()
        answer.append(count)

    return answer

# Time complexity: O(N)
# Space complexity: O(N)
