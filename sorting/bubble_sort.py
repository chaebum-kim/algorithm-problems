
def bubble_sort(x: list) -> list:

    end = len(x) - 1
    while end > 0:
        for i in range(0, end):
            if x[i] > x[i+1]:
                # Swap
                temp = x[i]
                x[i] = x[i+1]
                x[i+1] = temp

        end -= 1

    return x

# Time complexity: O(n^2)
# Space complexity: O(1)


if __name__ == '__main__':
    print(bubble_sort([2, 3, 1, 6, 7, 8]))
