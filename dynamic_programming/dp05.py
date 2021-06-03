''' Question: 등굣길
** https://programmers.co.kr/learn/courses/30/lessons/42898
'''


# Recursive solution
def solution1(m, n, puddles):

    def count_paths(x, y, memoize):
        if x >= m or y >= n or grid[x][y] == 1:
            return 0
        if (x, y) in memoize:
            return memoize[(x, y)]

        count = count_paths(x+1, y, memoize) + count_paths(x, y+1, memoize)
        memoize[(x, y)] = count

        return count

    grid = [[0] * n for i in range(m)]

    for x, y in puddles:
        grid[x-1][y-1] = 1

    memoize = {}
    memoize[(m-1, n-1)] = 1
    count = count_paths(0, 1, memoize) + count_paths(1, 0, memoize)

    return count % 1000000007


# Iterative solution
def solution2(m, n, puddles):

    def count_paths(x, y):
        up, left = 0, 0
        if x - 1 >= 0:
            up = grid[x-1][y]
        if y - 1 >= 0:
            left = grid[x][y-1]
        return up + left

    grid = [[1] * n for i in range(m)]

    for x, y in puddles:
        grid[x-1][y-1] = 0

    for i in range(m):
        for j in range(n):
            if grid[i][j] != 0 and (i, j) != (0, 0):
                grid[i][j] = count_paths(i, j)

    answer = count_paths(m-1, n-1)
    return answer % 1000000007
