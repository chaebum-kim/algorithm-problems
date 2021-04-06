
def quick_sort(x: list, left: int, right: int) -> list:

    if left < right:
        pivot = partition_on_pivot(x, left, right)
        quick_sort(x, left, pivot-1)
        quick_sort(x, pivot+1, right)


def partition_on_pivot(x: list, left: int, right: int) -> int:

    pivot = left

    # Partiton
    for i in range(left, right):
        if x[i] < x[right]:
            x[pivot], x[i] = x[i], x[pivot]
            pivot += 1

    x[pivot], x[right] = x[right], x[pivot]
    return pivot

# Time complexity: O(n^2), Θ(nlogn)
# Space complexity: O(logn)


if __name__ == '__main__':
    x = [3, 2, 1, 2, 10, 4, 6, 9, 8, 7]
    left = 0
    right = len(x) - 1
    quick_sort(x, left, right)
    print(x)
