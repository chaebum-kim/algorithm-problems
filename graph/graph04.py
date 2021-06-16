''' Question: 가장 먼 노드
*   https://programmers.co.kr/learn/courses/30/lessons/49189
'''

from collections import defaultdict, deque


def solution(n, edge):

    # Build adjacency list
    adj = defaultdict(list)
    for src, dest in edge:
        adj[src].append(dest)
        adj[dest].append(src)

    # BFS
    queue = deque([1])
    distance, length = -1, 0
    seen = {}

    while queue:
        if length == 0:
            length = len(queue)
            distance += 1

        current = queue.popleft()
        if current not in seen:
            seen[current] = distance
            for vertex in adj[current]:
                queue.append(vertex)

        length -= 1

    # Find the furthest nodes
    max_distance = max(seen.values())
    count = 0
    for vertex in range(1, n+1):
        if seen[vertex] == max_distance:
            count += 1

    return count
