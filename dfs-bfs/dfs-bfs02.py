''' Question: 네트워크
**  https://programmers.co.kr/learn/courses/30/lessons/43162
'''


# DFS
def solution(n, computers):

    def link(vertex, seen):
        if vertex in seen:
            return None
        seen.add(vertex)
        for linked in range(n):
            if computers[vertex][linked] == 1:
                link(linked, seen)

    seen = set()
    count = 0
    for vertex in range(n):
        if vertex not in seen:
            count += 1
            link(vertex, seen)

    return count
