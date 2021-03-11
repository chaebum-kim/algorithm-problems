''' Question:
*   Given a 2D array containing 0's(empty cell), 1's(fresh orange)) and 2's(rotten orange).
*   Every minute, all fresh orange immediately adjacent (4 directions) to rotten oranges will rot.
*   How many minutes must pass until all oranges are rotten?
'''


directions = [
    [-1, 0],
    [0, 1],
    [1, 0],
    [0, -1]
]


def minutes_to_rot(matrix: list) -> int:

    rotten_oranges = []
    count_fresh_oranges = 0
    mins = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 2:
                rotten_oranges.append([i, j])
            elif matrix[i][j] == 1:
                count_fresh_oranges += 1
    if not rotten_oranges and not count_fresh_oranges:
        return 0

    count_rotten_oranges = len(rotten_oranges)

    while rotten_oranges:
        if not count_rotten_oranges:
            count_rotten_oranges = len(rotten_oranges)
            mins += 1

        current = rotten_oranges.pop(0)
        count_rotten_oranges -= 1
        row = current[0]
        col = current[1]

        for direction in directions:
            next_row = row + direction[0]
            next_col = col + direction[1]
            if next_row in range(len(matrix)) and next_col in range(len(matrix[0]))\
                    and matrix[next_row][next_col] == 1:
                matrix[next_row][next_col] = 2
                count_fresh_oranges -= 1
                rotten_oranges.append([next_row, next_col])

    if count_fresh_oranges:
        return -1
    return mins

# Time complexity: O(n)
# Space complexity: O(n)


# Test
if __name__ == '__main__':
    matrix1 = [[2, 1, 1, 0, 0], [1, 1, 1, 0, 0],
               [0, 1, 1, 1, 1], [0, 1, 0, 0, 1]]
    matrix2 = [[1, 1, 0, 0, 0], [2, 1, 0, 0, 0],
               [0, 0, 0, 1, 2], [0, 1, 0, 0, 1]]

    print(minutes_to_rot(matrix1))
    print(minutes_to_rot(matrix2))
