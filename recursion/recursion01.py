''' Question:
*   Given an unsorted array, return the kth largest element.
*   It is the kth largest element in sorted order, not the kth distinct element.
'''

import sys
sys.path.insert(1, '/home/chaebum_kim/projects/problems/sorting')
from quick_sort import quick_sort, partition_on_pivot


# Using quick sort
def get_kth_largest(x: list, k: int) -> int:

    index_to_find = len(x) - k
    quick_sort(x, 0, len(x)-1)
    return x[index_to_find]

# Complexity: Same as quick sort


# Hoare's QuickSelect algorithm
def get_kth_largest2(x: list, k: int) -> int:

    index_to_find = len(x) - k
    quick_select(x, 0, len(x)-1, index_to_find)
    return x[index_to_find]


def quick_select(x: list, left: int, right: int, key: int):

    if left < right:
        pivot = partition_on_pivot(x, left, right)

        if key == pivot:
            return None
        elif key < pivot:
            return quick_select(x, left, pivot-1, key)
        else:
            return quick_select(x, pivot+1, right, key)

# Time complexity: O(n^2), Θ(n), Ω(n)
# Space complexity: O(1)


# Test
print(get_kth_largest([3, 2, 1, 2, 10, 4, 6, 9, 8, 7], 2))
print(get_kth_largest2([3, 2, 1, 2, 10, 4, 6, 9, 8, 7], 1))

