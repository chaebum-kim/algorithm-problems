''' Question: 행렬 테두리 회전하기
*   https://programmers.co.kr/learn/courses/30/lessons/77485
'''

DIRS = {
    'r': [0, 1],
    'd': [1, 0],
    'l': [0, -1],
    'u': [-1, 0]
}


def solution(rows, columns, queries):

    # Build original matrix
    matrix = [[0 for c in range(columns)] for r in range(rows)]
    for r in range(rows):
        for c in range(columns):
            matrix[r][c] = r * columns + c + 1

    result = []
    for q in queries:
        begin = [q[0]-1, q[1]-1]
        end = [q[2]-1, q[3]-1]
        row_range = sorted([begin[0], end[0]])
        col_range = sorted([begin[1], end[1]])
        result.append(rotate(matrix, begin, row_range, col_range))

    return result


def rotate(matrix, begin, row_range, col_range):

    min_ = matrix[begin[0]][begin[1]]
    prev = 0
    cur = begin
    d = 'r'

    while (True):
        r, c = cur
        min_ = min(min_, matrix[r][c])
        prev, matrix[r][c] = matrix[r][c], prev

        next_ = [r + DIRS[d][0], c + DIRS[d][1]]
        while not (row_range[0] <= next_[0] <= row_range[1] and
                   col_range[0] <= next_[1] <= col_range[1]):
            if d == 'r':
                d = 'd'
            elif d == 'd':
                d = 'l'
            elif d == 'l':
                d = 'u'
            else:
                d = 'r'
            next_ = [r + DIRS[d][0], c + DIRS[d][1]]

        cur = next_
        if cur == begin:
            break

    matrix[cur[0]][cur[1]] = prev
    return min_
