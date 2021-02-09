import unittest

''' Question:
*   Given a string, find the length of the longest substring without
*   repeating characters
'''


# Brute force solution
def getLongestSubstringLength(string):

    strlen = len(string)
    maxLength = 0

    # Loop through string
    for i in range(0, strlen):
        substring = {}
        currentLength = 0
        j = i

        while j < strlen and substring.get(string[j]) is None:
            substring[string[j]] = True
            currentLength += 1

            if currentLength > maxLength:
                maxLength = currentLength

            j += 1

    return maxLength

# Time complexity: O(n^2)
# Space complexity: O(n)


# Optimal solution
def getLongestSubstringLength2(string):

    strlen = len(string)

    if strlen <= 1:
        return strlen

    # Set start pointer and maxLength
    start = 0
    maxLength = 0
    seen = {}

    for end, char in enumerate(string):

        repeated = seen.get(char, -1)
        seen[char] = end

        if repeated >= start:
            start = repeated + 1
        else:
            maxLength = max([maxLength, end-start+1])

    return maxLength

# Time complexity: O(n)
# Space complexity: O(n)


# Test
class TestSolutions(unittest.TestCase):

    def test_brute_force_solution(self):
        self.assertEqual(getLongestSubstringLength("abccabb"), 3)
        self.assertEqual(getLongestSubstringLength("cccccc"), 1)
        self.assertEqual(getLongestSubstringLength(""), 0)
        self.assertEqual(getLongestSubstringLength("abcbda"), 4)

    def test_optimal_solution(self):
        self.assertEqual(getLongestSubstringLength2("abccabb"), 3)
        self.assertEqual(getLongestSubstringLength2("cccccc"), 1)
        self.assertEqual(getLongestSubstringLength2(""), 0)
        self.assertEqual(getLongestSubstringLength2("abcbda"), 4)


if __name__ == '__main__':
    unittest.main()
