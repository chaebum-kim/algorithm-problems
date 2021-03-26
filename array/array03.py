''' Question:
*   Given an array of integers representing an elevation map where the width of
*   each bar is 1, return how much rainwater can be trapped.
'''


# Brute force solution
def measure_rainwater_brute(nums: list) -> int:

    total = 0
    length = len(nums)
    for i, num in enumerate(nums):
        pl, pr = i-1, i+1
        left = right = 0

        while pl >= 0:
            left = max(left, nums[pl])
            pl -= 1
        while pr < length:
            right = max(right, nums[pr])
            pr += 1

        rainwater = min(left, right) - num
        if rainwater > 0:
            total += rainwater

    return total

# Time complexity: O(N^2)
# Space complexity: O(1)


# Optimal solution
def measure_rainwater_optimal(nums: list) -> int:

    total = 0
    left = right = 0
    pl, pr = 0, len(nums)-1

    while pl < pr:
        if nums[pl] < nums[pr]:
            left = max(left, nums[pl])
            rainwater = left - nums[pl]
            total += rainwater
            pl += 1
        else:
            right = max(right, nums[pr])
            rainwater = right - nums[pr]
            total += rainwater
            pr -= 1

    return total

# Time complexity: O(N)
# Space complexity: O(1)


# Test
if __name__ == '__main__':
    nums1 = [0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2]
    nums2 = []
    nums3 = [3]
    nums4 = [3, 4, 3]

    # Expected result: 8, 0, 0, 0
    print(measure_rainwater_brute(nums1))
    print(measure_rainwater_brute(nums2))
    print(measure_rainwater_brute(nums3))
    print(measure_rainwater_brute(nums4))

    print(measure_rainwater_optimal(nums1))
    print(measure_rainwater_optimal(nums2))
    print(measure_rainwater_optimal(nums3))
    print(measure_rainwater_optimal(nums4))
