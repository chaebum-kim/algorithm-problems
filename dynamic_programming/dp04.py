''' Question: 정수삼각형
** https://programmers.co.kr/learn/courses/30/lessons/43105
'''


def solution(triangle):

    height = len(triangle)

    for h in range(1, height):
        for i in range(h+1):
            if i == 0:
                triangle[h][i] += triangle[h-1][i]
            elif i == h:
                triangle[h][i] += triangle[h-1][i-1]
            else:
                triangle[h][i] += max(triangle[h-1][i-1], triangle[h-1][i])

    return max(triangle[-1])
