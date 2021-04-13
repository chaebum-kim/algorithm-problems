''' Question:
*   There are a total of n courses to take, labeled from 0 to n-1.
*   Some courses have prerequisite courses. This is expressed as a pair i.e.
*   [1, 0] which indicates you must take course 0 before taking course 1.
*   Given the total number of courses and an array of prerequisite pairs,
*   return if it is possible to finish all courses.
'''

from collections import deque


# Brute force solution
def can_finish_brute(n: int, prereqs: list) -> bool:

    # Build graph from prereqs
    adj_list = [[] for x in range(n)]
    for pair in prereqs:
        adj_list[pair[1]].append(pair[0])

    for course in range(n):
        q = deque()
        seen = {}
        q.extend(adj_list[course])

        while q:
            current = q.popleft()
            seen[current] = True

            if current == course:
                return False

            for next_course in adj_list[current]:
                if seen.get(next_course) is None:
                    q.append(next_course)

    return True

# Time complexity: O(p+N^3) // p = len(prereqs)
# Space complexity: O(N^2)


# Utilizing Topological Sort(for directed acyclic graph)
def can_finish_optimal(n: int, prereqs: list) -> bool:

    # Build graph from prereqs
    adj_list = [[] for x in range(n)]
    in_degrees = [0 for x in range(n)]
    for pair in prereqs:
        adj_list[pair[1]].append(pair[0])
        in_degrees[pair[0]] += 1

    stack = []
    for course, in_degree in enumerate(in_degrees):
        if in_degree == 0:
            stack.append(course)

    count = 0
    while stack:
        current = stack.pop()
        count += 1
        for next_course in adj_list[current]:
            in_degrees[next_course] -= 1
            if in_degrees[next_course] == 0:
                stack.append(next_course)

    return count == n

# Time complexity: O(p+N^2)
# Space complexity: O(N^2)
