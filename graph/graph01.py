''' Question:
*   A company has n employees with unique ID's from 0 to n-1. 
*   The head of the company has the ID headID. You will receive a managers array
*   where managers[i] is the ID of the manager for employee i. Each employee
*   has one direct manager. The company head has no manager(managers[headID] = -1).
*   It's guaranteed the subordination relationships will have a tree structure.
*   The head of the company watns to inform all employees of news.
*   He will inform direct subordinates who will inform their direct subordinates and so on
*   until everyone knows th news.
*   You will receive an informTime array where informTime[i] is the time it takes
*   for employee i to inform all their direct subordinates.
*   Return the total number of minutes it takes to inform all employees of the news.
*   https://leetcode.com/problems/time-needed-to-inform-all-employees/
'''


def num_of_minutes(n: int, managers: list, head_id: int, inform_time: int) -> int:
    def inform_employees(employee_id):
        if not adj_list[employee_id]:
            return 0

        max_time = 0
        for e in adj_list[employee_id]:
            max_time = max(max_time, inform_employees(e))
        return inform_time[employee_id] + max_time

    # Create adjacency list representing subordination relationships
    adj_list = [[] for x in range(n)]
    for e, m in enumerate(managers):
        if m != -1:
            adj_list[m].append(e)

    return inform_employees(head_id)

# Time complexity: O(N)
# Space complexity: O(N)
