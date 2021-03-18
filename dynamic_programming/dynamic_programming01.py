''' Question:
*   For a given staircase, the i-th step is assigned a non-negative cost
*   indicated by a cost array. Once you pay the cost for a step,
*   You can either climb one or two steps. Find the minimum cost
*   to reach the top of the staircase. Your first step can either be the first or second step.
'''


# Recursive solution
def find_minimum_cost1(cost: list) -> int:

    n = len(cost)
    return min([min_cost(cost, n-1), min_cost(cost, n-2)])


def min_cost(cost: list, i: int) -> int:

    if i < 0:
        return 0
    elif i == 0 or i == 1:
        return cost[i]

    return cost[i] + min([min_cost(cost, i-1), min_cost(cost, i-2)])

# Time complexity: O(2^n)
# Space complexity: O(N)


# Memoizing redundant recursive calls
def find_minimum_cost2(cost: list) -> int:

    n = len(cost)
    calculated = [None for x in range(n)]
    return min([min_cost2(cost, n-1, calculated),
                min_cost2(cost, n-2, calculated)])


def min_cost2(cost: list, i: int, calculated: list) -> int:

    if i < 0:
        return 0
    elif i == 0 or i == 1:
        return cost[i]

    if calculated[i] is not None:
        return calculated[i]

    calculated[i] = cost[i] + \
        min([min_cost2(cost, i-1, calculated), min_cost2(cost, i-2, calculated)])
    return calculated[i]

# Time complexity: O(N)
# Space complexity: O(N)


# Bottom-up approach
def find_minimum_cost3(cost: int) -> int:

    n = len(cost)
    if n == 0:
        return 0
    if n == 1:
        return cost[1]

    calculated = [None for x in range(n)]
    for i, value in enumerate(cost):
        if i < 2:
            calculated[i] = value
        else:
            calculated[i] = value + min([calculated[i-1], calculated[i-2]])
    return min([calculated[n-1], calculated[n-2]])

# Time complexity: O(N)
# Space complexity: O(N)


# Bottom-up optimization
def find_minimum_cost4(cost: int) -> int:

    n = len(cost)
    if n == 0:
        return 0
    if n == 1:
        return cost[1]

    two_step_before = cost[0]
    one_step_before = cost[1]

    for i in range(2, n):
        current = cost[i] + min([one_step_before, two_step_before])
        two_step_before = one_step_before
        one_step_before = current

    return min([one_step_before, two_step_before])

# Time complexity: O(N)
# Space complexity: O(1)


# Test
if __name__ == '__main__':
    cost = [20, 15, 30, 5]

    print(find_minimum_cost1(cost))
    print(find_minimum_cost2(cost))
    print(find_minimum_cost3(cost))
    print(find_minimum_cost4(cost))
