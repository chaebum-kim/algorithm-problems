''' Question:
*   Given an 2D array containing -1's(walls), 0's gates and INF's (empty room).
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


def fill_with_distance(matrix: list) -> list:

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == GATE:
                evaluate_distance_from_gate(matrix, row, col, 0)
    return matrix


def evaluate_distance_from_gate(matrix: list, row: int, col: int, distance: int):

    if row in range(len(matrix)) and col in range(len(matrix[0]))\
            and distance <= matrix[row][col]:
        matrix[row][col] = distance

        for direction in directions:
            evaluate_distance_from_gate(
                matrix, row+direction[0], col+direction[1], distance+1)

# Time complexity: O(n)
# Space complexity: O(n)


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
