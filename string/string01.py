''' Question:
*   Given two strings S and T, return if they equal when both are typed out.
*   Any '#' that appears in the string counts as a backspace.
*   https://leetcode.com/problems/backspace-string-compare/
'''

import itertools


# Brute force solution
def is_equal_brute(s: str, t: str) -> bool:
    def build_array(x: str) -> str:
        new_array = []
        for char in x:
            if char != '#':
                new_array.append(char)
            else:
                if new_array:
                    new_array.pop()
        return new_array

    return build_array(s) == build_array(t)

# Time complexity: O(a+b)
# Space complexity: O(a+b)


# Optimal solutions
def is_equal_optimal(s: str, t: str) -> bool:

    p1, p2 = len(s)-1, len(t)-1
    while p1 >= 0 or p2 >= 0:
        while p1 >= 0 and s[p1] == '#':
            skip = 1
            p1 -= 1
            while p1 >= 0 and skip > 0:
                if s[p1] == '#':
                    skip += 1
                else:
                    skip -= 1
                p1 -= 1
        while p2 >= 0 and t[p2] == '#':
            skip = 1
            p2 -= 1
            while p2 >= 0 and skip > 0:
                if t[p2] == '#':
                    skip += 1
                else:
                    skip -= 1
                p2 -= 1

        if p1 >= 0 and p2 >= 0:
            if s[p1] != t[p2]:
                return False
        elif (p1 >= 0 and p2 < 0) or (p1 < 0 and p2 >= 0):
            return False
        p1 -= 1
        p2 -= 1

    return True

# Time complexity: O(a+b)
# Space complexity: O(1)


def is_equal_optimal2(s: str, t: str) -> bool:
    def F(string):
        skip = 0
        for char in reversed(string):
            if char == '#':
                skip += 1
            elif skip > 0:
                skip -= 1
            else:
                yield char

    return all(x == y for x, y in itertools.zip_longest(F(s), F(t)))

# Time complexity: O(a+b)
# Space complexity: O(1)
