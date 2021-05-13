''' Question: 가장 큰 수
** https://programmers.co.kr/learn/courses/30/lessons/42746
'''

from functools import cmp_to_key


def solution(numbers):
    def compare(x, y):
        num1 = str(x) + str(y)
        num2 = str(y) + str(x)

        if num1 == num2:
            return 0
        elif num1 > num2:
            return 1
        else:
            return -1

    numbers.sort(key=cmp_to_key(compare), reverse=True)
    answer = ''.join(str(num) for num in numbers)

    if numbers[0] == 0:
        return '0'
    return answer
