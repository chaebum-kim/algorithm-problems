''' Question:
*   Given an array of integers, return the indices of the two
*   numbers that add up to a given target
*   https://leetcode.com/problems/two-sum/
'''


# Brute force solution
def find_two_sum_brute(nums: list, target: int) -> list:

    for i, num1 in enumerate(nums):
        for j, num2 in enumerate(nums[i+1:], i+1):
            if num1 + num2 == target:
                return [i, j]
    return None

# Time complexity: O(N^2)
# Space complexity: O(1)


# Optimal solution
def find_two_sum_optimal(nums: list, target: int) -> list:

    map_ = {}  # {number2: index of number1} where number1 + number2 = target
    for i, num in enumerate(nums):
        j = map_.get(num)
        if j is not None:
            return[j, i]
        else:
            map_[target-num] = i
    return None

# Time complexity: O(N)
# Space complexity: O(N)
