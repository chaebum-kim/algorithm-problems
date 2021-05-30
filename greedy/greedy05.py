''' Question: 섬 연결하기
**  https://programmers.co.kr/learn/courses/30/lessons/42861
'''

from collections import deque


# My solution
def solution1(n, costs):

    total = 0
    bridges = [[] for x in range(n)]
    for i, j, cost in costs:
        bridges[i].append(j)
        bridges[j].append(i)
        total += cost

    costs.sort(key=lambda x: x[2])

    while costs:
        # Remove the bridge if possible
        i, j, cost = costs.pop(-1)
        bridges[i].remove(j)
        bridges[j].remove(i)

        if is_connected(n, bridges):
            total -= cost
        else:
            bridges[i].append(j)
            bridges[j].append(i)

    return total


def is_connected(n, bridges):

    islands = deque([0])
    count = 1
    seen = set([0])

    while islands:
        current = islands.popleft()
        for neighbor in bridges[current]:
            if neighbor not in seen:
                seen.add(neighbor)
                islands.append(neighbor)
                count += 1

    return count == n


# Kruskal's Algorithm
def solution2(n, costs):

    parents = [x for x in range(n)]
    ranks = [0 for x in range(n)]
    total = 0

    costs.sort(key=lambda x: x[2])

    for x, y, cost in costs:
        root_x = find_root(x, parents)
        root_y = find_root(y, parents)
        if root_x != root_y:
            total += cost
            union(root_x, root_y, ranks, parents)

    return total


def find_root(x, parents):
    while x != parents[x]:
        x = parents[x]
    return x


def union(root_x, root_y, ranks, parents):
    if ranks[root_x] > ranks[root_y]:
        parents[root_y] = root_x
    else:
        parents[root_x] = root_y
        if ranks[root_x] == ranks[root_y]:
            ranks[root_y] += 1
