''' Question:
*   You are given an array of positive integers where each integer represents
*   the height of a vertical line on a chart. Find two lines which together
*   with x-axis forms a container that would hold the greates amount of water.
*   Return the area of water it would hold.
'''


# Brute force solution
def getMaxContainer(heights):

    maxArea = 0

    # Loop through heights
    length = len(heights)
    for i in range(0, length):
        for j in range(i + 1, length):
            # Compute height of container
            height = min([heights[i], heights[j]])

            # Compute width of container
            width = j - i

            # Compute area of container
            area = height * width

            # Compare area to maxArea
            if area > maxArea:
                maxArea = area

    return maxArea

# Time complexity: O(n^2)
# Space complexity: O(1)


# Optimized solution
def getMaxContainer2(heights):

    maxArea = 0

    # Set pointers on both ends of array
    p1 = 0
    p2 = len(heights) - 1

    # Loop until pointers meet
    while p1 < p2:
        # Compute height
        height = min([heights[p1], heights[p2]])

        # Compute width
        width = p2 - p1

        # Compute area
        area = height * width

        # Compare area to maxArea
        if area > maxArea:
            maxArea = area

        # Move pointer that points to smaller height towards center
        if heights[p1] < heights[p2]:
            p1 += 1
        else:
            p2 -= 1

    return maxArea

# Time complexity: O(n)
# Space complexity: O(1)


# Test
print(getMaxContainer([7, 1, 2, 3, 9]))
print(getMaxContainer([7]))
print(getMaxContainer([6, 9, 3, 4, 5, 8]))
print(getMaxContainer2([7, 1, 2, 3, 9]))
print(getMaxContainer2([7]))
print(getMaxContainer2([6, 9, 3, 4, 5, 8]))
