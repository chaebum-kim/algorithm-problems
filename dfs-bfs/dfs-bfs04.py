''' Question:  여행경로
*   https://programmers.co.kr/learn/courses/30/lessons/43164
'''

from collections import defaultdict


# DFS
def solution(tickets):

    n = len(tickets)
    tickets.sort(key=lambda x: x[1])

    routes = defaultdict(list)
    for x, y in tickets:
        routes[x].append(y)

    answer = []
    travel(1, n, "ICN", routes, answer)
    answer.append("ICN")
    answer.reverse()

    return answer


def travel(count, n, depart, routes, answer):

    if count > n:
        return True

    arrivals = [x for x in routes[depart]]

    for arrival in arrivals:
        routes[depart].remove(arrival)
        if travel(count+1, n, arrival, routes, answer):
            answer.append(arrival)
            return True
        routes[depart].append(arrival)

    return False
