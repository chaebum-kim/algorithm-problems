''' Question: 단속카메라
** https://programmers.co.kr/learn/courses/30/lessons/42884
'''


def solution(routes):

    routes.sort(key=lambda x: x[0])
    cctv = routes[0][1]
    count = 1

    for i in range(1, len(routes)):
        begin, end = routes[i]
        if begin <= cctv:
            cctv = min(end, cctv)
        else:
            cctv = end
            count += 1

    return count
