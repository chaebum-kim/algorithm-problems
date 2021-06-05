''' Question: 타겟 넘버
** https://programmers.co.kr/learn/courses/30/lessons/43165
'''

from collections import deque


# BFS
def solution1(numbers, target):

    queue = deque([0])
    for num in numbers:
        count = len(queue)
        for i in range(count):
            current = queue.popleft()
            queue.append(current+num)
            queue.append(current-num)

    return sum([1 for x in queue if x == target])


# DFS
def solution2(numbers, target):

    def count(num, i):
        if i == n-1:
            return num == target
        return count(num + numbers[i+1], i+1) + count(num - numbers[i+1], i+1)

    n = len(numbers)
    return count(0, -1)
