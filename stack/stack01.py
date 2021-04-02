''' Question:
*   Given an string containing only praentheses, determine if it is valid.
*   The string is valid if all parentheses close.
'''
from collections import deque
import unittest


def isValidParentheses(string: str) -> bool:

    leftBrackets = deque()
    match = {
        "{": "}",
        "[": "]",
        "(": ")"
    }

    for char in string:
        if match.get(char) is not None:
            leftBrackets.append(char)
        else:
            try:
                leftBracket = leftBrackets.pop()
                if char != match.get(leftBracket):
                    return False
            except:
                return False

    return not bool(leftBrackets)

# Time complexity: O(n)
# Space complexity: O(n)


class TestSolution(unittest.TestCase):
    def test_1(self):
        ''' Empty string returns True'''
        self.assertEqual(isValidParentheses(""), True)

    def test_2(self):
        ''' {([])} returns True '''
        self.assertEqual(isValidParentheses("{([])}"), True)

    def test_3(self):
        ''' {[]()} returns True '''
        self.assertEqual(isValidParentheses("{[]()}"), True)

    def test_4(self):
        ''' {([] returns False '''
        self.assertEqual(isValidParentheses("{([]"), False)


if __name__ == '__main__':
    unittest.main()
