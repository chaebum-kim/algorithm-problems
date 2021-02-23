
def selection_sort(x: list) -> list:
    for i in range(0, len(x)):
        min_ = i
        for j in range(i+1, len(x)):
            if x[j] < x[min_]:
                min_ = j

        # Swap
        temp = x[i]
        x[i] = x[min_]
        x[min_] = temp

    return x

# Time complexity: O(n^2)
# Space complexity: O(1)


if __name__ == '__main__':
    print(selection_sort([3, 2, 1, 5, 4, 9, 7]))
