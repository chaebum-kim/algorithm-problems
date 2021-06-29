''' Question: 괄호 변환
*   https://programmers.co.kr/learn/courses/30/lessons/60058
'''


match = {'(': ')', ')': '('}


def solution(p):

    if is_correct(p):
        return p
    return make_balance(p)


def make_balance(p):
    if p == '':
        return ''

    u, v = divide(p)
    if is_correct(u):
        return u + make_balance(v)
    else:
        return '(' + make_balance(v) + ')' + flip(u[1:-1])


def is_correct(p):
    stack = []
    for x in p:
        if x == '(':
            stack.append(x)
        else:
            if stack and match[x] == stack[-1]:
                stack.pop()
            else:
                return False
    return True


def divide(p):
    left, right, n = 0, 0, len(p)
    for i in range(n):
        if p[i] == '(':
            left += 1
        else:
            right += 1

        if left == right:
            break

    return p[:i+1], p[i+1:]


def flip(p):
    result = ''
    for x in p:
        result += match[x]
    return result
