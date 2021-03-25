''' Question:
*   You are given an array of positive integers where each integer represents
*   the height of a vertical line on a chart. Find two lines which together
*   with x-axis forms a container that would hold the greatest amount of water.
*   Return the area of water it would hold.
'''


# Brute force solution
def get_area_brute(heights: list) -> int:

    max_area = 0
    for i, num1 in enumerate(heights):
        for j, num2 in enumerate(heights[i+1:], i+1):
            height = min(num1, num2)
            width = j - i
            area = height * width
            max_area = max(max_area, area)
    return max_area

# Time complexity: O(N^2)
# Space complexity: O(1)


# Optimal solution
def get_area_optimal(heights: list) -> int:

    max_area = 0
    pl = 0
    pr = len(heights) - 1

    while pl < pr:
        height = min(heights[pl], heights[pr])
        width = pr - pl
        area = height * width
        max_area = max(max_area, area)
        if heights[pl] < heights[pr]:
            pl += 1
        else:
            pr -= 1
    return max_area

# Time complexity: O(N)
# Space complexity: O(1)


# Test
if __name__ == '__main__':
    heights1 = [1, 3, 6, 2, 5]
    heights2 = [1]

    # Expected result: 10, 0
    print(get_area_brute(heights1))
    print(get_area_brute(heights2))

    print(get_area_optimal(heights1))
    print(get_area_optimal(heights2))
