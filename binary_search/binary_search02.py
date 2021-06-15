''' Question: 징검다리
*   https://programmers.co.kr/learn/courses/30/lessons/43236
'''


def solution(distance, rocks, n):

    left, right = 0, distance
    rocks.sort()

    while left < right:
        middle = (left + right) // 2 + 1
        count = count_rocks(middle, rocks, distance)
        # If the number of rocks being removed are greater than n,
        # the answer must be smaller than the middle
        if count > n:
            right = middle - 1
        # If not, the answer must be greater or equal to the middle
        else:
            left = middle
    return left


def count_rocks(target, rocks, distance):
    begin, count = 0, 0
    for rock in rocks:
        if rock - begin < target:
            count += 1
        else:
            begin = rock

    if distance - begin < target:
        count += 1

    return count
