''' Question: 크레인 인형뽑기 게임
*   https://programmers.co.kr/learn/courses/30/lessons/64061
'''


def solution(board, moves):

    N = len(board[0])

    # Save the location of the first doll in each column
    locations = [0 for x in range(N)]
    for col in range(N):
        row = 0
        while row < N and board[row][col] == 0:
            row += 1
        locations[col] = row

    basket = []
    count = 0
    for m in moves:
        # Take out a doll if there is one
        if (row := locations[m-1]) < N:
            doll = board[row][m-1]
            board[row][m-1] = 0
            locations[m-1] = row + 1

            # Remove the last doll if it is of the same kind
            if basket and basket[-1] == doll:
                basket.pop()
                count += 2
            else:
                basket.append(doll)

    return count
