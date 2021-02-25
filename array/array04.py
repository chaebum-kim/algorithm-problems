''' Question:
*   Given an array of integers sorted in ascending order, return the
*   starting and ending index of a given target value in an array, i.e. [x,y].
*   Your solution should run in O(logn) time.
'''

import unittest


def find_target_range(nums: list, key: int) -> list:

    right = len(nums) - 1
    found = binary_search(nums, key, 0, right)
    start, end = found, found

    if found != -1:
        # Find starting index
        candidate = start
        while candidate != -1:
            start = candidate
            candidate = binary_search(nums, key, 0, start-1)

        # Find ending index
        candidate = end
        while candidate != -1:
            end = candidate
            candidate = binary_search(nums, key, end+1, right)

    return [start, end]

# Time complexity: O(logn)
# Space complexity: O(1)


def binary_search(nums: list, key: int, left: int, right: int) -> int:

    while left <= right:
        mid = int((left + right) / 2)
        if nums[mid] == key:
            return mid
        elif nums[mid] < key:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Time complexity: O(logn)
# Space complexity: O(1)


# Test
class TestSolution(unittest.TestCase):
    def test_1(self):
        self.assertEqual(find_target_range(
            [1, 3, 3, 5, 5, 5, 8, 9], 5), [3, 5])


if __name__ == '__main__':
    unittest.main()
