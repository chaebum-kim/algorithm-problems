''' Question:
*   Given a string, determine if it is almost a palindrome.
*   A string is almost a palindrome if it becomes a palindrome by removing 1 letter.
*   Consider only alphanumeric characters and ignore case sensitivity
'''

import re
import unittest


# My solution
def isAlmostPalindrome1(string):
    # Consider only alphanumeric characters
    string = re.sub(r"[^a-zA-Z0-9]", "", string).lower()

    # Set pointers
    pL = 0
    pR = len(string) - 1

    # Loop through string
    while pL < pR:

        if string[pL] != string[pR]:
            new = string[pL+1:pR+1]
            reversedNew = new[::-1]

            if new == reversedNew:
                return True

            new = string[pL:pR]
            reversedNew = new[::-1]

            if new == reversedNew:
                return True

            return False

        pL += 1
        pR -= 1

    return True

# Time complexity: O(n)
# Space complexity: O(n)


# Optimal Solution
def isValidSubPalindrome(string, pL, pR):
    while pL < pR:
        if string[pL] != string[pR]:
            return False

        pL += 1
        pR -= 1

    return True


def isAlmostPalindrome2(string):

    # Consider only alphanumeric characters
    string = re.sub(r"[^a-zA-Z0-9]", "", string).lower()

    # Set pointers
    pL = 0
    pR = len(string) - 1

    # Loop through string
    while pL < pR:

        if string[pL] != string[pR]:
            return isValidSubPalindrome(string, pL+1, pR) or isValidSubPalindrome(string, pL, pR-1)

        pL += 1
        pR -= 1

    return True

# Time complexity: O(n)
# Space complexity: O(1)


# Test
class TestSolution(unittest.TestCase):
    def test_isAlmostPalindrome1(self):
        self.assertEqual(isAlmostPalindrome1("race a car"), True)
        self.assertEqual(isAlmostPalindrome1("abccdba"), True)
        self.assertEqual(isAlmostPalindrome1("abcdefdba"), False)
        self.assertEqual(isAlmostPalindrome1(""), True)
        self.assertEqual(isAlmostPalindrome1("a"), True)
        self.assertEqual(isAlmostPalindrome1("ab"), True)
        self.assertEqual(isAlmostPalindrome1(
            "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"), True)

    def test_isAlmostPalindrome2(self):
        self.assertEqual(isAlmostPalindrome2("race a car"), True)
        self.assertEqual(isAlmostPalindrome2("abccdba"), True)
        self.assertEqual(isAlmostPalindrome2("abcdefdba"), False)
        self.assertEqual(isAlmostPalindrome2(""), True)
        self.assertEqual(isAlmostPalindrome2("a"), True)
        self.assertEqual(isAlmostPalindrome2("ab"), True)
        self.assertEqual(isAlmostPalindrome2(
            "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"), True)


if __name__ == '__main__':
    unittest.main()
