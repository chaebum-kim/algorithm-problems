''' Question: 튜플
*   https://programmers.co.kr/learn/courses/30/lessons/64065
'''


def solution(s):
    # Parse
    setofset = s[2:-2].split('},{')

    # Sort by the length of the set
    setofset.sort(key=len)

    tuple_ = []
    for set_ in setofset:
        set_ = [int(num) for num in set_.split(',')]
        tuple_.extend(list(set(set_) - set(tuple_)))
    return tuple_
