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
*   form employee i to inform all their direct subordinates.
*   Return the total number of minutes it takes to inform all employees of the news.
'''


def get_total_time(managers: list, head_id: int, inform_time: int) -> int:

    # Create adjacency list representing subordination relationships
    relationships = [[] for x in range(len(managers))]
    for subordinate, manager in enumerate(managers):
        if manager != -1:
            relationships[manager].append(subordinate)

    # Get total number of minutes it takes to inform the news
    return minutes_to_inform_news(relationships, head_id, inform_time)


def minutes_to_inform_news(relationships: list, current_id: int, inform_time: list):

    if not relationships[current_id]:
        return 0

    max_minutes = 0
    for subordinate in relationships[current_id]:
        max_minutes = max([max_minutes, minutes_to_inform_news(
            relationships, subordinate, inform_time)])

    return inform_time[current_id] + max_minutes

# Time complexity: O(n)
# Space complexity: O(n)


if __name__ == '__main__':

    head_id = 4
    managers = [2, 2, 4, 6, -1, 4, 4, 5]
    inform_time = [0, 0, 4, 0, 7, 3, 6, 0]
    print(get_total_time(managers, head_id, inform_time))

    head_id = 0
    managers = [-1]
    inform_time = [0]
    print(get_total_time(managers, head_id, inform_time))

    head_id = 6
    managers = [1, 2, 3, 4, 5, 6, -1]
    inform_time = [0, 6, 5, 4, 3, 2, 1]
    print(get_total_time(managers, head_id, inform_time))
