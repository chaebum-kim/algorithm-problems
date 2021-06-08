''' Question: 단어 변환
*   https://programmers.co.kr/learn/courses/30/lessons/43163
'''

from collections import deque


# BFS
def solution(begin, target, words):

    count, length = 0, 0
    queue = deque([begin])

    while queue:

        if length == 0:
            count += 1
            length = len(queue)

        current = queue.popleft()
        for word in words:
            if is_transformable(current, word):
                if word == target:
                    return count
                queue.append(word)
                words.remove(word)

        length -= 1

    return 0


def is_transformable(source, target):
    count = 0
    for i in range(len(source)):
        if source[i] != target[i]:
            count += 1
    return count == 1
