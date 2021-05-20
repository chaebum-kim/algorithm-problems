''' Question: 카펫
*   https://programmers.co.kr/learn/courses/30/lessons/42842
'''

import math


def solution(brown, yellow):
    target = int((brown - 4) / 2)
    min_width = math.ceil(target/2)

    for inner_width in range(min_width, target):
        inner_height = target - inner_width
        if inner_width * inner_height == yellow:
            return [inner_width+2, inner_height+2]
