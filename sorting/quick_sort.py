
def quick_sort(x: list, left: int, right: int) -> list:

    if left < right:
        pivot = partition_on_pivot(x, left, right)
        quick_sort(x, left, pivot-1)
        quick_sort(x, pivot+1, right)


def partition_on_pivot(x: list, left: int, right: int) -> int:

    i, j = left, left

    # Partiton
    while j != right:
        if x[j] < x[right]:
            # Swap
            x[i], x[j] = x[j], x[i]
            i += 1

        j += 1

    x[i], x[right] = x[right], x[i]

    # Return pivot index
    return i

# Time complexity: O(n^2), Θ(nlogn)
# Space complexity: O(logn)


if __name__ == '__main__':
    x = [3, 2, 1, 2, 10, 4, 6, 9, 8, 7]
    left = 0
    right = len(x) - 1
    quick_sort(x, left, right)
    print(x)
