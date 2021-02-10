''' Question:
*   Given a string, determine if it is a palindrome, considering only alphanumeric
*   characters and ignoring case sensitivity
'''
import unittest
import re


def isPalindrome1(string):

    # Replace non-alphanumeric characters with nothing
    string = re.sub(r"[^a-zA-Z0-9]", "", string).lower()

    # Set pointers
    pL = 0
    pR = len(string) - 1

    while pL < pR:
        if string[pL] != string[pR]:
            return False

        pL += 1
        pR -= 1

    return True


def isPalindrome2(string):

    # Replace non-alphanumeric characters with nothing
    string = re.sub(r"[^a-zA-Z0-9]", "", string).lower()

    # Set pointers
    length = len(string)

    if length % 2 == 0:
        pL = int(length/2) - 1
        pR = pL + 1
    else:
        pL = pR = int(length/2)

    while pL >= 0 and pR < length:
        if string[pL] != string[pR]:
            return False

        pL -= 1
        pR += 1

    return True


def isPalindrome3(string):

    # Replace non-alphanumeric characters with nothing
    string = re.sub(r"[^a-zA-Z0-9]", "", string).lower()

    # Reverse string
    reversedStr = string[::-1]

    if string != reversedStr:
        return False

    return True


class TestSolutions(unittest.TestCase):
    def test_solution_1(self):
        self.assertEqual(isPalindrome1("aabaa"), True)
        self.assertEqual(isPalindrome1("aabbaa"), True)
        self.assertEqual(isPalindrome1("abc"), False)
        self.assertEqual(isPalindrome1(""), True)
        self.assertEqual(isPalindrome1("a"), True)
        self.assertEqual(isPalindrome1("A man, a plan, a canal: Panama"), True)

    def test_solution_2(self):
        self.assertEqual(isPalindrome2("aabaa"), True)
        self.assertEqual(isPalindrome2("aabbaa"), True)
        self.assertEqual(isPalindrome2("abc"), False)
        self.assertEqual(isPalindrome2(""), True)
        self.assertEqual(isPalindrome2("a"), True)
        self.assertEqual(isPalindrome2("A man, a plan, a canal: Panama"), True)

    def test_solution_3(self):
        self.assertEqual(isPalindrome3("aabaa"), True)
        self.assertEqual(isPalindrome3("aabbaa"), True)
        self.assertEqual(isPalindrome3("abc"), False)
        self.assertEqual(isPalindrome3(""), True)
        self.assertEqual(isPalindrome3("a"), True)
        self.assertEqual(isPalindrome3("A man, a plan, a canal: Panama"), True)


if __name__ == '__main__':
    unittest.main()
