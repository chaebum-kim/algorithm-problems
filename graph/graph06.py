''' Question: 방의 개수
*   https://programmers.co.kr/learn/courses/30/lessons/49190
'''

from collections import defaultdict, deque


DIRS = [
    [-1, 0],  # up
    [-1, 1],  # upper-right
    [0, 1],  # right
    [1, 1],  # down-right
    [1, 0],  # down
    [1, -1],  # down-left
    [0, -1],  # left
    [-1, -1]  # up-left
]


def solution1(arrows):

    edges = defaultdict(set)
    prev = (0, 0)
    count = 0

    for arrow in arrows:
        row = prev[0] + DIRS[arrow][0]
        col = prev[1] + DIRS[arrow][1]
        cur = (row, col)

        if not is_visited(prev, cur, edges):
            # If the current point meets another edge
            if cur in edges:
                count += 1
            # If the current edge is diagonal and crossed
            if is_diagonal(arrow) and is_crossed(prev, cur, edges):
                count += 1

        # Update the edges
        edges[prev].add(cur)
        edges[cur].add(prev)

        prev = cur

    return count


def is_visited(src, dest, edges):
    if src in edges and dest in edges[src]:
        return True
    return False


def is_diagonal(arrow):
    if arrow in (1, 3, 5, 7):
        return True
    return False


def is_crossed(prev, cur, edges):
    dest = (cur[0], prev[1])
    src = (prev[0], cur[1])
    if src in edges and dest in edges[src]:
        return True
    return False


# 오일러의 다면체 정리 (2차원): v-e+f = 1
def solution2(arrows):

    prev = (0, 0)
    edges = defaultdict(set, {prev: set()})
    v, e = 1, 0

    for arrow in arrows:
        for i in range(2):
            row = prev[0] + DIRS[arrow][0]
            col = prev[1] + DIRS[arrow][1]
            cur = (row, col)

            # Count the new vertex
            if cur not in edges:
                v += 1

            # Count the new edge
            if cur not in edges[prev]:
                e += 1

            # Update the edges
            edges[prev].add(cur)
            edges[cur].add(prev)

            prev = cur

    return 1 + e - v
