''' Question:
*   Given an 2D array containing -1's(walls), 0's (gates)g and INF's (empty room).
*   Fill each empty room with the number of steps to the nearest gate.
*   If it is impossible to reach a gate, leave INF as the value.
*   INF is equal to 2147483647.
'''

directions = [
    [-1, 0],
    [0, 1],
    [1, 0],
    [0, -1]
]

WALL = -1
GATE = 0
INF = 2147483647


def fill_with_distance(grid: list) -> list:
    def count_steps(grid, row, col, step):
        if 0 <= row < m and 0 <= col < n and grid[row][col] >= step:
            grid[row][col] = step
            step += 1
            for direction in directions:
                count_steps(grid, row+direction[0], col+direction[1], step)

    m, n = len(grid), len(grid[0])
    for row in range(m):
        for col in range(n):
            if grid[row][col] == GATE:
                count_steps(grid, row, col, 0)
    return grid

# Time complexity: O(N)
# Space complexity: O(N)


# Test
if __name__ == '__main__':
    matrix1 = [[INF, -1, 0, INF], [INF, INF, INF, -1],
               [INF, -1, INF, -1], [0, -1, INF, INF]]
    matrix2 = [[INF, -1, 0, INF], [-1, INF, INF, -1],
               [INF, -1, INF, -1], [0, -1, INF, INF]]

    for i in range(len(matrix1)):
        matrix1 = fill_with_distance(matrix1)
        print(matrix1[i])
    print()

    for i in range(len(matrix2)):
        matrix2 = fill_with_distance(matrix2)
        print(matrix2[i])
    print()
