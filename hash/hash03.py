''' Question: 위장
*   https://programmers.co.kr/learn/courses/30/lessons/42578/
'''


def solution(clothes):

    kinds = {}
    for c, kind in clothes:
        if kind in kinds:
            kinds[kind] += 1
        else:
            kinds[kind] = 1

    total = 0
    for count in kinds.values():
        # Add combinations so far * new kind + wearing clothes of new kind only
        total += (total*count + count)

    return total

# Time complexity: O(N)
# Space complexity: O(N)
