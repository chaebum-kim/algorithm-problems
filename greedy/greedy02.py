''' Question: 조이스틱
*   https://programmers.co.kr/learn/courses/30/lessons/42860
'''


def solution(name):

    alphabets = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6,
                 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12,
                 'N': 13, 'O': 12, 'P': 11, 'Q': 10, 'R': 9, 'S': 8,
                 'T': 7, 'U': 6, 'V': 5, 'W': 4, 'X': 3, 'Y': 2, 'Z': 1}

    cursor, answer = 0, 0

    moves = [alphabets[alpha] for alpha in name]

    while True:

        # Change the alphabet
        answer += moves[cursor]
        moves[cursor] = 0

        if sum(moves) == 0:
            break

        # Find the next location to change
        left, right = 1, 1
        # Search the left side of the cursor
        while moves[cursor-left] == 0:
            left += 1
        # Search the right side of the cursor
        while moves[cursor+right] == 0:
            right += 1

        # Move the cursor
        if left < right:
            cursor -= left
        else:
            cursor += right
        answer += min(left, right)

    return answer
