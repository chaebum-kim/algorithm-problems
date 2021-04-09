''' Question:
*   Given a 2D array containing only 1's(land) and 0's(water), count the number of islands.
*   An island is land connected horizontally or vertically.
*   https://leetcode.com/problems/number-of-islands/
'''
from collections import deque

directions = [
    [-1, 0],
    [0, 1],
    [1, 0],
    [0, -1]
]


# Depth-first search
def count_islands_dfs(grid: List[List[str]]) -> int:
    def exclude_island(grid, row, col):
        if not (0 <= row < m and 0 <= col < n):
            return None
        if grid[row][col] == '1':
            grid[row][col] = '0'
            for direction in directions:
                exclude_island(grid, row+direction[0], col+direction[1])

    count = 0
    m, n = len(grid), len(grid[0])
    for row in range(m):
        for col in range(n):
            if grid[row][col] == '1':
                exclude_island(grid, row, col)
                count += 1

    return count


# Breadth-first search
def count_islands_bfs(grid: List[List[str]]) -> int:
    def exclude_old_island(grid, row, col):
        q = deque([[row, col]])
        while q:
            current = q.popleft()
            row = current[0]
            col = current[1]

            if 0 <= row < m and 0 <= col < n and grid[row][col] == '1':
                grid[row][col] = '0'
                for direction in directions:
                    q.append([row+direction[0], col+direction[1]])

        count = 0
        m, n = len(grid), len(grid[0])
        for row in range(m):
            for col in range(n):
                if grid[row][col] == '1':
                    count += 1
                    exclude_old_island(grid, row, col)

        return count

# Time complexity: O(M*N) // M = row, N = column
# Space compleity: O(max(M,N))
