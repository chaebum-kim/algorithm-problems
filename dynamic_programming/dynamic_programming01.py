''' Question:
*   For a given staircase, the i-th step is assigned a non-negative cost
*   indicated by a cost array. Once you pay the cost for a step,
*   You can either climb one or two steps. Find the minimum cost
*   to reach the top of the staircase. Your first step can either be the first or second step.
*   https://leetcode.com/problems/min-cost-climbing-stairs/
'''


# Recursive solution
def min_cost_climbing_stairs1(cost: list) -> int:
    def min_cost_so_far(n):
        if n < 0:
            return 0
        if 0 <= n <= 1:
            return cost[n]
        return cost[n] + min(min_cost_so_far(n-1), min_cost_so_far(n-2))

    last = len(cost)
    return min(min_cost_so_far(last-1), min_cost_so_far(last-2))

# Time complexity: O(2^N)
# Space complexity: O(N)


# Memoizing redundant recursive calls
def min_cost_climbing_stairs2(cost: list) -> int:
    def min_cost_so_far(n, dp):
        if n < 0:
            return 0
        if 0 <= n <= 1:
            return cost[n]

        if dp.get(n) is not None:
            return dp.get(n)

        result = cost[n] + min(min_cost_so_far(n-1, dp),
                               min_cost_so_far(n-2, dp))
        dp[n] = result
        return result

    last = len(cost)
    dp = {}
    return min(min_cost_so_far(last-1, dp), min_cost_so_far(last-2, dp))

# Time complexity: O(N)
# Space complexity: O(N)


# Bottom-up approach
def min_cost_climbing_stairs3(cost: int) -> int:

    length = len(cost)
    if length <= 1:
        return 0

    prev_prev, prev = cost[0], cost[1]
    for i in range(2, length):
        min_cost_so_far = min(prev_prev, prev) + cost[i]
        prev_prev = prev
        prev = min_cost_so_far

    return min(prev_prev, prev)

# Time complexity: O(N)
# Space complexity: O(1)
