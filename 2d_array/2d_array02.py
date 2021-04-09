''' Question:
*   Given a 2D array containing 0's(empty cell), 1's(fresh orange) and 2's(rotten orange).
*   Every minute, all fresh orange immediately adjacent (4 directions) to rotten oranges will rot.
*   How many minutes must pass until all oranges are rotten?
*   https://leetcode.com/problems/rotting-oranges/
'''

from collections import deque


directions = [
    [-1, 0],
    [0, 1],
    [1, 0],
    [0, -1]
]


def minutes_to_rot(grid: List[List[int]]) -> int:

    m, n = len(grid), len(grid[0])
    rotten_oranges = deque()
    count_fresh = 0
    for row in range(m):
        for col in range(n):
            if grid[row][col] == 1:
                count_fresh += 1
            elif grid[row][col] == 2:
                rotten_oranges.append([row, col])

    if rotten_oranges and not count_fresh:
        return 0

    mins = 0
    while rotten_oranges:
        if count_fresh:
            mins += 1

        count_rotten = len(rotten_oranges)
        for i in range(count_rotten):
            current = rotten_oranges.popleft()
            row = current[0]
            col = current[1]
            for direction in directions:
                adj_row = row + direction[0]
                adj_col = col + direction[1]
                if 0 <= adj_row < m and 0 <= adj_col < n and grid[adj_row][adj_col] == 1:
                    grid[adj_row][adj_col] = 2
                    rotten_oranges.append([adj_row, adj_col])
                    count_fresh -= 1

    if count_fresh:
        return -1
    return mins

# Time complexity: O(N)
# Space complexity: O(N)
