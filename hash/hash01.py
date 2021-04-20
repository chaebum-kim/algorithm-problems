''' Question: 완주하지 못한 선수
*   https://programmers.co.kr/learn/courses/30/lessons/42576
'''


def solution(participant, completion):

    comp = {}
    for name in completion:
        if name not in comp:
            comp[name] = 1
        else:
            comp[name] += 1

    for name in participant:
        if name not in comp or comp[name] == 0:
            return name
        comp[name] -= 1

# Time complexity: O(N)
# Space complexity: O(N)
