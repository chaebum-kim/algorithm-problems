''' 수식최대화
*   https://programmers.co.kr/learn/courses/30/lessons/67257
'''

from itertools import permutations


OP = {'+': 0, '-': 0, '*': 0}


def solution(expression):

    # Parse the expression
    exp = parse(expression)

    # Get the operators
    operators = []
    for key in OP.keys():
        if OP[key] > 0:
            operators.append(key)

    answer = 0
    for p in permutations(operators):
        temp = exp
        for operator in p:
            temp = calculate(temp, operator)
        answer = max(answer, abs(temp[-1]))

    return answer


def calculate(exp, operator):
    new_exp = []
    i, N = 0, len(exp)
    while i < N:
        if exp[i] != operator:
            new_exp.append(exp[i])
            i += 1
        else:
            x = new_exp.pop()
            y = exp[i+1]
            if operator == '*':
                new_exp.append(x*y)
            elif operator == '+':
                new_exp.append(x+y)
            else:
                new_exp.append(x-y)
            i += 2

    return new_exp


def parse(expression):
    exp = []
    string = ''
    for c in expression:
        if c not in OP:
            string += c
        else:
            OP[c] += 1
            exp.append(int(string))
            exp.append(c)
            string = ''
    exp.append(int(string))
    return exp
