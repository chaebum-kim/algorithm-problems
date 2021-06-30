''' Question:
*   Given a string, find the length of the longest substring without
*   repeating characters
*   https://leetcode.com/problems/longest-substring-without-repeating-characters/
'''


# Brute force solution
def get_longest_substring_brute(s: str) -> int:

    max_length = 0
    strlen = len(s)
    for start in range(strlen):
        seen = {}
        length = 0
        i = start

        while i < strlen and seen.get(s[i]) is None:
            seen[s[i]] = True
            length += 1
            i += 1

        max_length = max(max_length, length)

    return max_length

# Time complexity: O(N^2)
# Space complexity: O(N)


# Optimal solution
def get_longest_substring_optimal(s: str) -> int:

    max_length = start = 0
    seen = {}

    for end, char in enumerate(s):
        # If character is repeated, update the starting index
        if seen.get(char, -1) >= start:
            start = seen[char] + 1

        seen[char] = end
        max_length = max(max_length, end-start+1)

    return max_length

# Time complexity: O(N)
# Space complexity: O(N)
