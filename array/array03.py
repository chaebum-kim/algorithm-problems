import unittest

''' Question:
*   Given an array of integers representing an elevation map where the width of
*   each bar is 1, return how much rainwater can be trapped.
'''


# Brute force solution
def measureRainwater(nums):

    total = 0

    # Loop through numbers
    length = len(nums)
    for i in range(0, length):

        # Initialize maxL, maxR
        maxL = 0
        maxR = 0

        # Set pointers
        pL = i - 1
        pR = i + 1

        # Find the maximum height on the left side
        while pL >= 0:
            if nums[pL] > maxL:
                maxL = nums[pL]
            pL -= 1

        # Find the maximum height on the right side
        while pR < length:
            if nums[pR] > maxR:
                maxR = nums[pR]
            pR += 1

        # Calculate trapped rainwater on current index
        currentWater = min([maxL, maxR]) - nums[i]

        # If currentWater is postivie, add it to the total
        if currentWater > 0:
            total += currentWater

    return total

# Time complexity: O(n^2)
# Space complexity: O(1)


# Optimal solution
def measureRainwater2(nums):

    total = 0
    maxLeft = 0
    maxRight = 0

    # Set pointers
    pL = 0
    pR = len(nums) - 1

    # Iterate until two pointers meet
    while pL < pR:
        # The right wall is formed
        if nums[pL] <= nums[pR]:
            # If there is left wall and container can be formed
            if nums[pL] < maxLeft:
                currentWater = maxLeft - nums[pL]
                total += currentWater
            # If not, update maxLeft
            else:
                maxLeft = nums[pL]

            # Move pointer inwards
            pL += 1

        # The left wall is formed
        else:
            # If there is right wall and container can be formed
            if nums[pR] < maxRight:
                currentWater = maxRight - nums[pR]
                total += currentWater
            # If not, update maxRight
            else:
                maxRight = nums[pR]

            # Move pointer inwards
            pR -= 1

    return total

# Time complexity: O(n)
# Space comlexity: O(1)


# Test
class Test(unittest.TestCase):

    def test_brute_force_solution(self):
        self.assertEqual(measureRainwater(
            [0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2]), 8)
        self.assertEqual(measureRainwater([]), 0)
        self.assertEqual(measureRainwater([3]), 0)
        self.assertEqual(measureRainwater([3, 4, 3]), 0)

    def test_optimal_solution(self):
        self.assertEqual(measureRainwater2(
            [0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2]), 8)
        self.assertEqual(measureRainwater2([]), 0)
        self.assertEqual(measureRainwater2([3]), 0)
        self.assertEqual(measureRainwater2([3, 4, 3]), 0)


if __name__ == '__main__':
    unittest.main()
