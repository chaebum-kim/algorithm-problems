''' Question:
*   Given a linked list, return it in reverse
*   https://leetcode.com/problems/reverse-linked-list/
'''


class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


def reverse_linked_list(head: ListNode) -> ListNode:

    reversed_ = None
    current = head
    while current is not None:
        next_ = current.next
        current.next = reversed_
        reversed_ = current
        current = next_
    return reversed_

# Time complexity: O(N)
# Space complexity: O(1)
