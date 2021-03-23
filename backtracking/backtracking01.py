''' Question:
*   Create a function that solves for any 9x9 sudoku puzzle given.
'''


def solve_sudoku(puzzle: list):
    def get_box_id(row, col):
        row = (row // 3) * 3
        col = col // 3
        return row + col

    def backtracking(puzzle, row, col, row_check, col_check, box_check):
        if row == len(puzzle) or col == len(puzzle):
            return True

        if puzzle[row][col] is not None:
            if col == len(puzzle) - 1:
                if backtracking(puzzle, row+1, 0, row_check, col_check, box_check):
                    return True
            else:
                if backtracking(puzzle, row, col+1, row_check, col_check, box_check):
                    return True
        else:
            for current in range(1, 10):
                # Add current value to the puzzle
                puzzle[row][col] = current

                # Validate the puzzle
                box_id = get_box_id(row, col)
                if not row_check[row].get(current) and not col_check[col].get(current) \
                        and not box_check[box_id].get(current):
                    row_check[row][current] = True
                    col_check[col][current] = True
                    box_check[box_id][current] = True

                    if col == len(puzzle) - 1:
                        if backtracking(puzzle, row+1, 0, row_check, col_check, box_check):
                            return True
                    else:
                        if backtracking(puzzle, row, col+1, row_check, col_check, box_check):
                            return True

                    # Remove current value from the puzzle
                    row_check[row][current] = False
                    col_check[col][current] = False
                    box_check[box_id][current] = False

                puzzle[row][col] = None

    # Initialize checks for row, column, and column
    row_check = [{} for x in range(9)]
    col_check = [{} for x in range(9)]
    box_check = [{} for x in range(9)]

    for row in range(9):
        for col in range(9):
            if puzzle[row][col] is not None:
                value = puzzle[row][col]
                box_id = get_box_id(row, col)
                row_check[row][value] = True
                col_check[col][value] = True
                box_check[box_id][value] = True

    backtracking(puzzle, 0, 0, row_check, col_check, box_check)
    return puzzle

# Time complexity: O(9!^9)
# Space complexity: O(81)


# Test
if __name__ == '__main__':
    puzzle = [
        [5, 3, None, None, 7, None, None, None, None],
        [6, None, None, 1, 9, 5, None, None, None],
        [None, 9, 8, None, None, None, None, 6, None],
        [8, None, None, None, 6, None, None, None, 3],
        [4, None, None, 8, None, 3, None, None, 1],
        [7, None, None, None, 2, None, None, None, 6],
        [None, 6, None, None, None, None, 2, 8, None],
        [None, None, None, 4, 1, 9, None, None, 5],
        [None, None, None, None, 8, None, None, 7, 9]
    ]

    puzzle2 = [
        [5, 5, None, None, 7, None, None, None, None],
        [6, None, None, 1, 9, 5, None, None, None],
        [None, 9, 8, None, None, None, None, 6, None],
        [8, None, None, None, 6, None, None, None, 3],
        [4, None, None, 8, None, 3, None, None, 1],
        [7, None, None, None, 2, None, None, None, 6],
        [None, 6, None, None, None, None, 2, 8, None],
        [None, None, None, 4, 1, 9, None, None, 5],
        [None, None, None, None, 8, None, None, 7, 9]
    ]

    print(solve_sudoku(puzzle))
    print(solve_sudoku(puzzle2))
