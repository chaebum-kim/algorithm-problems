''' Question:
*   Given a string, determine if it is almost a palindrome.
*   A string is almost a palindrome if it becomes a palindrome by removing 1 letter.
*   Consider only alphanumeric characters and ignore case sensitivity
*   https://leetcode.com/problems/valid-palindrome-ii/
'''

import re


# Brute force solution
def is_almost_palindrome_brute(s: str) -> bool:

    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    pl, pr = 0, len(s)-1

    while pl < pr:
        if s[pl] != s[pr]:
            new = s[pl+1:pr+1]
            reversed_new = new[::-1]
            if new == reversed_new:
                return True

            new = s[pl:pr]
            reversed_new = new[::-1]
            if new == reversed_new:
                return True

            return False

        pl += 1
        pr -= 1

    return True

# Time complexity: O(N)
# Space complexity: O(N)


# Optimal Solution
def is_almost_palindrome_optimal(s: str) -> bool:
    def is_valid(s: str, pl: int, pr: int) -> bool:
        while pl < pr:
            if s[pl] != s[pr]:
                return False
            pl += 1
            pr -= 1
        return True

    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    pl, pr = 0, len(s) - 1

    while pl < pr:
        if s[pl] != s[pr]:
            return is_valid(s, pl+1, pr) or is_valid(s, pl, pr-1)
        pl += 1
        pr -= 1

    return True


# Time complexity: O(N)
# Space complexity: O(1)
