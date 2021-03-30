''' Question:
*   Given an array of integers sorted in ascending order, return the
*   starting and ending index of a given target value in an array, i.e. [x,y].
*   Your solution should run in O(logn) time.
*   https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
'''


# Solution
def get_target_range(nums: list, target: int) -> list:
    def binary_search(nums: list, target: int, low: int, high: int) -> int:
        while low <= high:
            mid = int((low+high)/2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1

    length = len(nums)
    if length < 1:
        return [-1, -1]

    mid = binary_search(nums, target, 0, length-1)
    if mid == -1:
        return [-1, -1]

    start = end = mid
    temp = binary_search(nums, target, 0, start-1)
    while temp != -1:
        start = temp
        temp = binary_search(nums, target, 0, start-1)

    temp = binary_search(nums, target, end+1, length-1)
    while temp != -1:
        end = temp
        temp = binary_search(nums, target, end+1, length-1)

    return [start, end]

# Time complexity: O(logN)
# Space complexity: O(1)
