''' Question:
*   Given a string only containing round brackets '(' and ')' and lower chase characters,
*   remove the least amount of brackets so the string is valid.
*   A string is considered valid if it is empty or if there are brackets, they all close
'''
from collections import deque
import unittest


def makeValidString(string: str) -> str:

    leftBrackets = deque()
    stringToList = list(string)

    for i, char in enumerate(stringToList):
        if char == "(":
            leftBrackets.append(i)
        elif char == ")":
            if leftBrackets:
                leftBrackets.pop()
            else:
                stringToList[i] = ""

    while leftBrackets:
        stringToList[leftBrackets.pop()] = ""

    return "".join(stringToList)

# Time complexity: O(n)
# Space complexity: O(n)


class TestSolution(unittest.TestCase):
    def test_1(self):
        ''' a)bc(d) returns abc(d)'''
        self.assertEqual(makeValidString("a)bc(d)"), "abc(d)")

    def test_2(self):
        ''' (ab(c)d returns ab(c)d '''
        self.assertEqual(makeValidString("(ab(c)d"), "ab(c)d")

    def test_3(self):
        ''' ))(( returns empty string '''
        self.assertEqual(makeValidString("))(("), "")


if __name__ == '__main__':
    unittest.main()
