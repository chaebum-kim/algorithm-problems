
directions = [
    [-1, 0],  # Up
    [0, 1],  # Right
    [1, 0],  # Down
    [0, -1]  # Left
]


# Depth first search
def depth_first_search(matrix: list) -> list:

    values = []
    seen = [[False for x in range(len(matrix[0]))] for y in range(len(matrix))]

    traverse(matrix, 0, 0, values, seen)

    return values


def traverse(matrix: list, row: int, col: int, values: list, seen: list):

    if row not in range(0, len(matrix)) or col not in range(0, len(matrix[0])) or seen[row][col]:
        return None

    values.append(matrix[row][col])
    seen[row][col] = True

    for direction in directions:
        traverse(matrix, row+direction[0], col+direction[1], values, seen)

# Time complexity: O(n)
# Space complexity: O(n)


def breadth_first_search(matrix: list) -> list:

    if not matrix:
        return []

    values = []
    seen = [[False for x in range(len(matrix[0]))] for y in range(len(matrix))]
    q = [[0, 0]]

    while q:
        current = q.pop(0)
        row = current[0]
        col = current[1]

        if not seen[row][col]:
            values.append(matrix[row][col])
            seen[row][col] = True

            for direction in directions:
                next_row = row + direction[0]
                next_col = col + direction[1]
                if next_row in range(0, len(matrix)) and next_col in range(0, len(matrix[0])) and not seen[next_row][next_col]:
                    q.append([next_row, next_col])

    return values

# Time complexity: O(n)
# Space complexity: O(n)


# Test
if __name__ == '__main__':

    nums1 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15],
             [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
    nums2 = [[1]]
    nums3 = []

    print(depth_first_search(nums1))
    print(depth_first_search(nums2))
    print(depth_first_search(nums3))

    print(breadth_first_search(nums1))
    print(breadth_first_search(nums2))
    print(breadth_first_search(nums3))
