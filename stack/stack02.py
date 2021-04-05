''' Question:
*   Given a string only containing round brackets '(' and ')' and lower case characters,
*   remove the least amount of brackets so the string is valid.
*   A string is considered valid if it is empty or if there are brackets, they all close
*   https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
'''


def remove_to_make_valid(s: str) -> str:

    stack = []
    s = list(s)

    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                s[i] = ''

    while stack:
        s[stack.pop()] = ''

    new_s = ''.join(s)

    return new_s

# Time complexity: O(N)
# Space complexity: O(N)
