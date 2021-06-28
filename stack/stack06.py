''' Question: 짝지어 제거하기
*   https://programmers.co.kr/learn/courses/30/lessons/12973
'''


def solution(s):

    stack = []
    for c in s:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)

    return 0 if stack else 1
