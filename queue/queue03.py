''' Question: 프린터
*   https://programmers.co.kr/learn/courses/30/lessons/42587
'''

from collections import deque


def solution(priorities, location):
    waiting = deque([x for x in range(len(priorities))])
    count = 0

    while waiting:
        current = waiting.popleft()
        if any(priorities[current] < priorities[doc] for doc in waiting):
            waiting.append(current)
        else:
            count += 1
            if current == location:
                return count

# Time complexity: O(N^2)
# Space complexity: O(N)
