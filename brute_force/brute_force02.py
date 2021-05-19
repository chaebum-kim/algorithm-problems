''' Question: 소수 찾기
*   https://programmers.co.kr/learn/courses/30/lessons/42839
'''


from itertools import permutations


def solution(numbers):

    count = 0
    seen = set()

    for length in range(1, len(numbers)+1):
        for permut in permutations(numbers, length):
            num = int(''.join(permut))
            if num not in seen:
                if is_prime(num):
                    count += 1
                seen.add(num)
    return count


def is_prime(num):

    if num < 2:
        return False

    for divisor in range(2, int(num**0.5) + 1):
        if num % divisor == 0:
            return False

    return True
