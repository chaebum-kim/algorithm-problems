''' Question:
*   Given a limited list and numbers m and n, return it back with only
*   positions m to n in reverse
*   https://leetcode.com/problems/reverse-linked-list-ii/
'''


class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


def partial_reverse(head: ListNode, m: int, n: int) -> ListNode:

    reversed_ = None
    current = head
    position = 1

    while position < m:
        start = current
        current = current.next
        position += 1

    end = current

    while position <= n:
        next_ = current.next
        current.next = reversed_
        reversed_ = current
        current = next_
        position += 1

    end.next = current

    if m > 1:
        start.next = reversed_
    else:
        head = reversed_

    return head

# Time complexity: O(N)
# Space complexity: O(1)
