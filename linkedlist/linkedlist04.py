''' Question:
*   Cycle detection
'''
from SLinkedList import Node, SLinkedList


# Brute force solution
def isCycledList1(linkedlist: SLinkedList) -> Node:

    current = linkedlist.head
    seenNodes = set()

    while current is not None and current not in seenNodes:
        seenNodes.add(current)
        current = current.next

    ret = current or False

    # Return starting node of cycled or False if list is not cycled
    return ret

# Time complexity: O(n)
# Space complexity: O(n)


# Floyd's Tortoise and Hare Algorithm
def isCycledList2(linkedlist: SLinkedList) -> Node:
    tortoise = linkedlist.head
    hare = tortoise
    flag = False  # To execute the loop at least once

    # Get meeting point
    while tortoise != hare or not flag:
        if hare is None or hare.next is None:
            return False

        flag = True
        tortoise = tortoise.next
        hare = hare.next.next

    # Get starting point
    tortoise = linkedlist.head
    while tortoise != hare:
        tortoise = tortoise.next
        hare = hare.next

    return tortoise

# Time complexity: O(n)
# Space complexity: O(1)


# Test
cycledlist = SLinkedList().generateList(8)
start = cycledlist.getNode(3)
cycledlist.tail.next = start

noncycledlist = SLinkedList().generateList(8)

print(isCycledList1(cycledlist).key)
print(isCycledList1(noncycledlist))

print(isCycledList2(cycledlist).key)
print(isCycledList2(noncycledlist))
