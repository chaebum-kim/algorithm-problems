
def insertion_sort(x: list) -> list:
    for i in range(1, len(x)):
        key = x[i]
        j = i - 1
        while j >= 0 and key < x[j]:
            x[j+1] = x[j]
            j -= 1

        # Insert
        x[j+1] = key

    return x

# Time complexity: O(n^2) // O(n) when almost sorted(best case)
# Space complexity: O(1)


if __name__ == '__main__':
    print(insertion_sort([3, 2, 1, 5, 4, 9, 7]))
