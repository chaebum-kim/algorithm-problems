''' Question: N으로 표현
** https://programmers.co.kr/learn/courses/30/lessons/42895
'''


def solution(N, target):

    if target == N:
        return 1

    numbers_sets = [set() for i in range(8)]
    numbers_sets[0].add(N)

    for count in range(1, 8):
        numbers = numbers_sets[count]
        numbers.add(int(''.join([str(N)] * (count+1))))

        for first in range(int(count/2)+1):
            second = count - 1 - first
            for x in numbers_sets[first]:
                for y in numbers_sets[second]:
                    results = [x + y, x * y, x-y, y-x]
                    if y != 0:
                        results.append(int(x/y))
                    if x != 0:
                        results.append(int(y/x))
                    numbers.update(results)

                    if target in numbers:
                        return count + 1

    return -1
