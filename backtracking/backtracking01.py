''' Question:
*   Create a function that solves for any 9x9 sudoku puzzle given.
*   https://leetcode.com/problems/sudoku-solver/
'''


def solve_sudoku(board: list):
    def get_box_id(r, c):
        return (r//3)*3 + c//3

    def is_valid_value(r, c, box_id, value):
        if value in rows[r] or value in cols[c] or value in boxes[box_id]:
            return False
        return True

    def backtracking(r, c):
        if r >= 9:
            return True
        if r < 9 and c >= 9:
            return backtracking(r+1, 0)
        if board[r][c] != '.':
            return backtracking(r, c+1)

        for num in range(1, 10):
            num = str(num)
            board[r][c] = num
            box_id = get_box_id(r, c)
            if is_valid_value(r, c, box_id, num):
                rows[r].add(num)
                cols[c].add(num)
                boxes[box_id].add(num)

                if backtracking(r, c+1):
                    return True

                rows[r].remove(num)
                cols[c].remove(num)
                boxes[box_id].remove(num)

            board[r][c] = '.'

    rows = [set() for x in range(9)]
    cols = [set() for x in range(9)]
    boxes = [set() for x in range(9)]

    for r in range(9):
        for c in range(9):
            if (val := board[r][c]) != '.':
                rows[r].add(val)
                cols[c].add(val)
                boxes[get_box_id(r, c)].add(val)

    backtracking(0, 0)

# Time complexity: O(9!^9)
# Space complexity: O(81)
