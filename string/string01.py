import unittest
import itertools

''' Question:
*   Given two strings S and T, return if they equal when both are typed out.
*   Any '#' that appears in the string counts as a backspace.
'''


# Brute force solution
def compareStrings(S, T):

    def buildString(string):
        builtArray = []

        for char in string:
            if char != "#":
                builtArray.append(char)
            else:
                if len(builtArray) > 0:
                    builtArray.pop()

        return builtArray

    return buildString(S) == buildString(T)

# Time complexity: O(a+b)
# Space complexity: O(a+b)


# Optimal solution
def compareStrings2(S, T):
    def F(string):
        skip = 0
        for char in reversed(string):
            if char == '#':
                skip += 1
            elif skip > 0:
                skip -= 1
            else:
                yield char

    return all(x == y for x, y in itertools.zip_longest(F(S), F(T)))

# Time complexity: O(a+b)
# Space complexity: O(1)


# Test
class TestCompareStrings(unittest.TestCase):

    def test_brute_force_solution(self):
        self.assertEqual(compareStrings("ab#z", "az#z"), True)
        self.assertEqual(compareStrings("abc#d", "acc#c"), False)
        self.assertEqual(compareStrings("x#y#z#", "a#"), True)
        self.assertEqual(compareStrings("a###b", "b"), True)
        self.assertEqual(compareStrings("Ab#z", "ab#z"), False)

    def test_optimal_solution(self):
        self.assertEqual(compareStrings2("ab#z", "az#z"), True)
        self.assertEqual(compareStrings2("abc#d", "acc#c"), False)
        self.assertEqual(compareStrings2("x#y#z#", "a#"), True)
        self.assertEqual(compareStrings2("a###b", "b"), True)
        self.assertEqual(compareStrings2("Ab#z", "ab#z"), False)


if __name__ == '__main__':
    unittest.main()
