
def breadth_first_search(adjacency_list: list) -> list:

    seen = {}
    values = []
    q = [0]

    while q:
        current = q.pop(0)
        values.append(current)
        seen[current] = True

        for connection in adjacency_list[current]:
            if not seen.get(connection):
                q.append(connection)

    return values


def depth_first_search(adjacency_list: list) -> list:

    values = []
    traverse_vertex(adjacency_list, 0, values, {})
    return values


def traverse_vertex(adjacency_list: list, vertex: int, values: list, seen: dict):

    values.append(vertex)
    seen[vertex] = True

    for connection in adjacency_list[vertex]:
        if not seen.get(connection):
            traverse_vertex(adjacency_list, connection, values, seen)


# Test
if __name__ == '__main__':
    adjacency_list = [
        [1, 3],
        [0],
        [3, 8],
        [0, 4, 5, 2],
        [3, 6],
        [3],
        [4, 7],
        [6],
        [2]
    ]

    print(breadth_first_search(adjacency_list))
    print(depth_first_search(adjacency_list))
