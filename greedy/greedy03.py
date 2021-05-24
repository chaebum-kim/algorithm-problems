''' Question: 큰 수 만들기
*   https://programmers.co.kr/learn/courses/30/lessons/42883
'''


# Brute force solution
def solution1(number, k):

    for i in range(k):
        j, n = 0, len(number)
        while j < n - 1 and number[j] >= number[j+1]:
            j += 1
        number = number[:j] + number[j+1:]

    return number


# Optimal solution
def solution2(number, k):

    stack = [number[0]]
    for num in number[1:]:
        while stack > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)

    if k != 0:
        stack = stack[:-k]

    return ''.join(stack)
