''' Question:
*   There are a total of n courses to take, labeled from 0 to n-1.
*   Some courses have prerequisite courses. This is expressed as a pair i.e.
*   [1, 0] which indicates you must take course 0 before taking course 1.
*   Given the total number of courses and an array of prerequisite pairs,
*   return if it is possible to finish all courses.
'''


# Brute force solution
def is_valid_course1(n: int, prereqs: list) -> bool:

    # Build graph from prereqs
    adj_list = [[] for x in range(n)]
    for pair in prereqs:
        adj_list[pair[1]].append(pair[0])

    q1 = [x for x in range(n)]
    q2 = []

    for vertex in range(n):
        q = []
        seen = {}
        for connection in adj_list[vertex]:
            q.append(connection)

        while q:
            current = q.pop(0)
            seen[current] = True

            if current == vertex:
                return False

            for connection in adj_list[current]:
                if not seen.get(connection):
                    q.append(connection)

    return True

# Time complexity: O(p+n^3)
# Space complexity: O(n^2)


def is_valid_course2(n: int, prereqs: list) -> bool:

    # Build graph from prereqs
    adj_list = [[] for x in range(n)]
    indegrees = [0 for x in range(n)]
    for pair in prereqs:
        adj_list[pair[1]].append(pair[0])
        indegrees[pair[0]] += 1

    stack = []
    for vertex, indegree in enumerate(indegrees):
        if indegree == 0:
            stack.append(vertex)

    count = 0
    while stack:
        current = stack.pop()
        count += 1
        for connection in adj_list[current]:
            indegrees[connection] -= 1
            if indegrees[connection] == 0:
                stack.append(connection)

    return count == n


# Test
if __name__ == '__main__':
    n1 = 6
    prereqs1 = [[1, 0], [2, 1], [2, 5], [0, 3], [4, 3], [3, 5], [4, 5]]

    n2 = 7
    prereqs2 = [[0, 3], [1, 0], [2, 1], [4, 5], [6, 4], [5, 6]]

    print(is_valid_course1(n1, prereqs1))
    print(is_valid_course1(n2, prereqs2))
    print(is_valid_course2(n1, prereqs1))
    print(is_valid_course2(n2, prereqs2))
