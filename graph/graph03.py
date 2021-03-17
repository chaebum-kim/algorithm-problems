''' Question:
*   There are n network nodes labelled 1 to N. Given a times array, containing
*   edges represented by arrays [u, v, w] where u is the source node,
*   v is the target node, and w is the time taken to travel from the souce node
*   to the target node. Send a signal from node k, return how long it takes
*   for all nodes to receive the signal. Retrun -1 if it's impossible.
'''

import math
import importlib.util
spec = importlib.util.spec_from_file_location(
    "priority_queue", "/home/chaebum_kim/projects/problems/queue/priority_queue.py")
priority_queue = importlib.util.module_from_spec(spec)
spec.loader.exec_module(priority_queue)


# Dijkstra's algorithm
def newtwork_delay_time1(n: int, k: int, times: list) -> int:

    # Build adjacency list from times
    adj_list = [[] for x in range(n)]
    for time in times:
        source = time[0] - 1
        target = time[1] - 1
        weight = time[2]
        adj_list[source].append([target, weight])

    # Initialize distances
    distances = [math.inf for x in range(n)]
    distances[k-1] = 0

    # Initialize min_heap
    min_heap = priority_queue.PriorityQueue(
        comparator=lambda a, b: distances[a] < distances[b])
    min_heap.push(k-1)

    while not min_heap.is_empty():
        current = min_heap.pop()
        for connection in adj_list[current]:
            target = connection[0]
            weight = connection[1]
            if distances[current] + weight < distances[target]:
                distances[target] = distances[current] + weight
                min_heap.push(target)

    result = max(distances)
    return -1 if result == math.inf else result

# Time complexity: O(ElogN) // E = number of edges
# Space complexity: O(E+N)


# Bellman-Ford Algorithm (When weight can be negative, no negative cycle)
def newtwork_delay_time2(n: int, k: int, times: list) -> int:

    # Initialize distances
    distances = [math.inf for x in range(n)]
    distances[k-1] = 0

    # Calculate opitmal distances
    for i in range(n-1):
        count = 0
        for time in times:
            source = time[0] - 1
            target = time[1] - 1
            weight = time[2]
            if distances[source] + weight < distances[target]:
                distances[target] = distances[source] + weight
                count += 1

        if count == 0:
            break

    result = max(distances)
    return -1 if result == math.inf else result

# Time complexity: O(NE)
# Space complexity: O(N)


# Test
if __name__ == '__main__':
    n1 = 5
    k1 = 1
    times1 = [[1, 2, 9], [1, 4, 2], [2, 5, 1], [4, 2, 4],
              [4, 5, 6], [3, 2, 3], [5, 3, 7], [3, 1, 5]]

    n2 = 3
    k2 = 2
    times2 = [[2, 3, 4]]

    n3 = 3
    k3 = 1
    times3 = [[1, 2, 8], [3, 1, 3]]

    print(newtwork_delay_time1(n1, k1, times1))
    print(newtwork_delay_time1(n2, k2, times2))
    print(newtwork_delay_time1(n3, k3, times3))

    print(newtwork_delay_time2(n1, k1, times1))
    print(newtwork_delay_time2(n2, k2, times2))
    print(newtwork_delay_time2(n3, k3, times3))
