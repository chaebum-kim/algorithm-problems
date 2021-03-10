''' Question:
*   Given a 2D array containing only 1's(land) and 0's(water),
*   count the number of islands. An island is land connected 
*    horizontally or vertically.
'''

directions = [
    [-1, 0],
    [0, 1],
    [1, 0],
    [0, -1]
]


def count_islands(matrix: list) -> int:

    count = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 1:
                count += 1
                exclude_old_island(matrix, row, col)

    return count


def exclude_old_island(matrix: list, row: int, col: int):

    matrix[row][col] = 0
    q = [[row, col]]

    while q:
        current = q.pop(0)
        row = current[0]
        col = current[1]

        for direction in directions:
            next_row = row + direction[0]
            next_col = col + direction[1]

            if next_row in range(len(matrix)) and next_col in range(len(matrix[0]))\
                    and matrix[next_row][next_col] == 1:
                matrix[next_row][next_col] = 0
                q.append([next_row, next_col])

# Time complexity: O(m*n) // m = row, n = column
# Space compleity: O(max(m,n))


# Test
if __name__ == '__main__':
    matrix1 = [[1, 1, 1, 1, 0], [1, 1, 0, 1, 0],
               [1, 1, 0, 0, 1], [0, 0, 0, 1, 1]]
    matrix2 = [[0, 1, 0, 1, 0], [1, 0, 1, 0, 1],
               [0, 1, 1, 1, 0], [1, 0, 1, 0, 1]]
    matrix3 = []
    matrix4 = [[], []]

    print(count_islands(matrix1))
    print(count_islands(matrix2))
    print(count_islands(matrix3))
    print(count_islands(matrix4))
