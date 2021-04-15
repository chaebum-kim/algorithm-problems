''' Question:
*   There are n network nodes labelled 1 to N. Given a times array, containing
*   edges represented by arrays [u, v, w] where u is the source node,
*   v is the target node, and w is the time taken to travel from the souce node
*   to the target node. Send a signal from node k, return how long it takes
*   for all nodes to receive the signal. Retrun -1 if it's impossible.
*   https://leetcode.com/problems/network-delay-time/
'''

import math
from queue import PriorityQueue


# Dijkstra's algorithm(for directed, weighted graph)
def newtwork_delay_time_dijkstra(n: int, k: int, times: list) -> int:

    # Build adjacency list from times
    adj_list = [[] for x in range(n)]
    for u, v, w in times:
        adj_list[u-1].append([v-1, w])

    # Initiailize distances
    distances = [math.inf for x in range(n)]
    distances[k-1] = 0

    # Initialize min heap
    pq = PriorityQueue()
    pq.put((distances[k-1], k-1))

    while not pq.empty():
        current = pq.get()[1]
        for target, weight in adj_list[current]:
            new_distance = distances[current] + weight
            if new_distance < distances[target]:
                distances[target] = new_distance
                pq.put((distances[target], target))

    result = max(distances)
    return -1 if result == math.inf else result

# Time complexity: O(ElogN) // E = number of edges
# Space complexity: O(E+N)


# Bellman-Ford Algorithm (When weight can be negative, no negative cycle)
def newtwork_delay_time_bellmanford(n: int, k: int, times: list) -> int:

    # Initialize distances
    distances = [math.inf for x in range(n)]
    distances[k-1] = 0

    for i in range(n-1):
        count = 0
        for source, target, weight in times:
            new_distance = distances[source-1] + weight
            if new_distance < distances[target-1]:
                distances[target-1] = new_distance
                count += 1

        if not count:
            break

    result = max(distances)
    return -1 if result == math.inf else result

# Time complexity: O(NE)
# Space complexity: O(N)
