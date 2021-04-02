''' Question:
*   Cycle detection
*   https://leetcode.com/problems/linked-list-cycle-ii/
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Brute force solution
def detect_cycle_brute()

 seen = set()
  current = head
   while current is not None:
        if current in seen:
            return current
        seen.add(current)
        current = current.next

    return None

# Time complexity: O(N)
# Space complexity: O(N)


# Floyd's Tortoise and Hare Algorithm
def detect_cycle_optimal(head: ListNode) -> ListNode:

    t = h = head
    while True:
        if t is None or t.next is None:
            return None
        if h.next is None or h.next.next is None:
            return None

        t = t.next
        h = h.next.next
        if t == h:
            break

    t = head
    while t != h:
        t = t.next
        h = h.next
    return t

# Time complexity: O(N)
# Space complexity: O(1)
