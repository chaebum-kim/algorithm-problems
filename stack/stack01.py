''' Question:
*   Given a string containing only parentheses, determine if it is valid.
*   The string is valid if all parentheses close.
*   https://leetcode.com/problems/valid-parentheses/
'''


def is_valid_parentheses(s: str) -> bool:

    left_brackets = []
      match = {
           '{': '}',
            '[': ']',
            '(': ')'
           }

       for char in s:
            if match.get(char) is not None:
                left_brackets.append(char)
            else:
                left = left_brackets.pop() if left_brackets else ''
                if char != match.get(left):
                    return False

        return not bool(left_brackets)

# Time complexity: O(N)
# Space complexity: O(N)
