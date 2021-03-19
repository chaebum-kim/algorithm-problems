''' Question:
*   On a given nxn chessboard, a knight piece will start at the r-th row
*   and c-th column. The kight will ateempt to make k moves.
*   A knight can move in 8 possible ways. Each move will choose one of these
*   8 at random. The knight continues moving until it finishes k moves
*   or it moves off the chessboard. Return the probability that the
*   knight is on the chessboard after it finishes moving.
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
def on_board_prob1(n: int, k: int, r: int, c: int) -> float:
    def knight_prob(n: int, k: int, r: int, c: int) -> float:
        if r not in range(n) or c not in range(n):
            return 0
        if k == 0:
            return 1

        result = 0
        for direction in DIRECTIONS:
            new_row = r + direction[0]
            new_col = c + direction[1]
            result += knight_prob(n, k-1, new_row, new_col) / 8

        return result

    return knight_prob(n, k, r, c)

# Time complexity: O(8^k)
# Space complexity: O(8^k)


# Memoizing
def on_board_prob2(n: int, k: int, r: int, c: int) -> float:
    def knight_prob(n: int, k: int, r: int, c: int, calculated: dict) -> float:

        if r not in range(n) or c not in range(n):
            return 0
        if k == 0:
            return 1

        if calculated[k][r][c] is not None:
            return calculated[k][r][c]

        result = 0
        for direction in DIRECTIONS:
            new_row = r + direction[0]
            new_col = c + direction[1]
            result += knight_prob(n, k-1, new_row, new_col, calculated) / 8
        calculated[k][r][c] = result
        return result

    calculated = []
    for step in range(k+1):
        calculated.append([[None for x in range(n)] for y in range(n)])
    return knight_prob(n, k, r, c, calculated)

# Time complexity: O(N^2*k)
# Space complexity: O(N^2*k)


# Iterative solution
def on_board_prob3(n: int, k: int, r: int, c: int) -> float:

    calculated = []
    for step in range(k+1):
        calculated.append([[0 for x in range(n)] for y in range(n)])
    calculated[0][r][c] = 1

    for i in range(1, k+1):
        for row in range(n):
            for col in range(n):
                for direction in DIRECTIONS:
                    prev_row = row + direction[0]
                    prev_col = col + direction[1]
                    if prev_row in range(n) and prev_col in range(n):
                        calculated[i][row][col] += \
                            calculated[i-1][prev_row][prev_col] / 8

    result = 0
    for row in calculated[k]:
        result += sum(row)
    return result

# Time complexity: O(N^2*k)
# Space complexity: O(N^2*k)


# Optimize iterative solution
def on_board_prob4(n: int, k: int, r: int, c: int) -> float:

    prev_board = [[0 for x in range(n)] for y in range(n)]
    prev_board[r][c] = 1

    for i in range(k):
        current_board = [[0 for x in range(n)] for y in range(n)]
        for row in range(n):
            for col in range(n):
                for direction in DIRECTIONS:
                    prev_row = row + direction[0]
                    prev_col = col + direction[1]
                    if 0 <= prev_row < n and 0 <= prev_col < n:
                        current_board[row][col] += prev_board[prev_row][prev_col] / 8
        prev_board = current_board

    return sum(map(sum, prev_board))

# Time complexity: O(N^2*k)
# Space complexity: O(N^2)


# Test
if __name__ == '__main__':

    # answer = 0.015625
    n = 3
    k = 3
    r = 0
    c = 0

    print(on_board_prob1(n, k, r, c))
    print(on_board_prob2(n, k, r, c))
    print(on_board_prob3(n, k, r, c))
    print(on_board_prob4(n, k, r, c))
