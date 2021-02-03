''' Question:
    Given an array of integers, return the indices of the two
    numbers that add up to a given target '''


# My solution
def findPair(nums, target):
    
    length = len(nums)

    # Loop through an array of nums
    for i in range(0, length):
        for j in range(i + 1, length):
            if nums[j] == target - nums[i]:
                return [i, j]

    # If there is no solution, return null
    return None

# Time complexity: O(n^2)
# Space complexity: O(1)


# Optimized solution
def findPair2(nums, target):

    length = len(nums)

    # Loop through an array of nums
    numsMap = {}
    for i in range(0, length):
        # Get map value of number
        mapValue = numsMap.get(nums[i])

        # If map value of number exists, return indexes
        if mapValue is not None:
            return [mapValue, i]
        # If not, save number to find as key and index of number as value
        else:
            numsMap[target-nums[i]] = i

    # If there is no solution, return null
    return None

# Time complexity: O(n)
# Space complexity: O(n)
