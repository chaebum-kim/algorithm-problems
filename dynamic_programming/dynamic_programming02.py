''' Question:
*   On a given nxn chessboard, a knight piece will start at the r-th row
*   and c-th column. The kight will attempt to make k moves.
*   A knight can move in 8 possible ways. Each move will choose one of these
*   8 at random. The knight continues moving until it finishes k moves
*   or it moves off the chessboard. Return the probability that the
*   knight is on the chessboard after it finishes moving.
*   https://leetcode.com/problems/knight-probability-in-chessboard/
'''

DIRECTIONS = [
    [-1, -2],
    [-2, -1],
    [-2, 1],
    [-1, 2],
    [1, -2],
    [2, -1],
    [2, 1],
    [1, 2],
]


# Recursive solution
def knight_prob1(n: int, k: int, r: int, c: int) -> float:
    def prob_so_far(n, k, r, c):
        if not (0 <= r < n and 0 <= c < n):
            return 0
        if k == 0:
            return 1

        result = 0
        for direction in DIRECTIONS:
            next_row, next_col = r + direction[0], c + direction[1]
            result += prob_so_far(n, k-1, next_row, next_col) / 8

        return result

    return prob_so_far(n, k, r, c)

# Time complexity: O(8^k)
# Space complexity: O(8^k)


# Memoizing
def knight_prob2(n: int, k: int, r: int, c: int) -> float:
    def prob_so_far(n, k, r, c, dp):

        if r not in range(n) or c not in range(n):
            return 0
        if k == 0:
            return 1

        if dp[k][r][c] is not None:
            return dp[k][r][c]

        result = 0
        for direction in DIRECTIONS:
            next_row, next_col = r + direction[0], c+direction[1]
            result += prob_so_far(n, k-1, next_row, next_col, dp) / 8
        dp[k][r][c] = result
        return result

    dp = []
    for step in range(k+1):
        dp.append([[None for x in range(n)] for y in range(n)])
    return prob_so_far(n, k, r, c, dp)

# Time complexity: O(N^2*k)
# Space complexity: O(N^2*k)


# Iterative Solution
def knight_prob3(n: int, k: int, r: int, c: int) -> float:

    prev = [[0 for x in range(n)] for y in range(n)]
    prev[r][c] = 1
    knights = {(r, c)}

    for i in range(k):
        current = [[0 for x in range(n)] for y in range(n)]
        next_knights = set()
        while knights:
            row, col = knights.pop()
            for direction in DIRECTIONS:
                next_row, next_col = row+direction[0], col+direction[1]
                if 0 <= next_row < n and 0 <= next_col < n:
                    current[next_row][next_col] += prev[row][col] / 8
                    next_knights.add((next_row, next_col))
        prev = current
        knights = next_knights

    return sum(map(sum, prev))

# Time complexity: O(N^2*k)
# Space complexity: O(N^2)
