
def merge_sort(x: list) -> list:

    length = len(x)

    if length == 1:
        return x

    # Split the list
    half = int(length/2)
    left = x[0:half]
    right = x[half:length]

    # Merge the list
    return merge(merge_sort(left), merge_sort(right))


def merge(left: list, right: list) -> list:

    left_length = len(left)
    right_length = len(right)
    merged_list = []

    i = 0
    j = 0

    while i < left_length and j < right_length:
        if left[i] <= right[j]:
            merged_list.append(left[i])
            i += 1
        else:
            merged_list.append(right[j])
            j += 1

    merged_list.extend(left[i:])
    merged_list.extend(right[j:])

    return merged_list

# Time complexity: O(nlogn)
# Space complexity: O(n)


if __name__ == '__main__':
    print(merge_sort([3, 2, 1, 5, 10, 4, 9, 8, 7]))
