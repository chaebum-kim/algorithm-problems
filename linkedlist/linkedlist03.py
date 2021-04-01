''' Question:
*   Given a doubly linked list, list nodes also have a child property that can point to
*   a separate doubly linked list. These child lists can also have one or more child
*   doubly linked lists of their own, and so on.
*   Return the list as a single level flattened doubly linked list
*   https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/
'''


class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


def flatten_list(head: Node) -> Node:

    current = head
    while current is not None:
        if current.child is not None:
            # Find the last node of child list
            last_child = current.child
            while last_child.next is not None:
                last_child = last_child.next

            # Link last child node to the next node
            last_child.next = current.next
            if last_child.next is not None:
                last_child.next.prev = last_child

            # Link child node to the current node
            current.next = current.child
            current.next.prev = current
            current.child = None
        current = current.next

    return head

# Time complexity: O(N)
# Space complexity: O(1)
