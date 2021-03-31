''' Question:
*   Given a s, determine if it is a palindrome, considering only alphanumeric
*   characters and ignoring case sensitivity
*   https://leetcode.com/problems/valid-palindrome/
'''

import re


def is_valid_palindrome1(s: str) -> bool:

    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    pl, pr = 0, len(s)-1

    while pl <= pr:
        if s[pl] != s[pr]:
            return False
        pl += 1
        pr -= 1

    return True


def is_valid_palindrome2(s: str) -> bool:

    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    length = len(s)
    if length % 2 == 0:
        pl = int(length/2) - 1
        pr = pl + 1
    else:
        pl = pr = int(length/2)

    while pl >= 0 and pr < length:
        if s[pl] != s[pr]:
            return False
        pl -= 1
        pr += 1

    return True


def is_valid_palindrome3(s: str) -> bool:

    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

    reversed_s = s[::-1]
    if s != reversed_s:
        return False

    return True
