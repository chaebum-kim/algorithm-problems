''' Question:
*   Given a doubly linked list, list nodes also have a child property that can point to
*   a separate doubly linked list. These child lists can also have one or more child
*   doubly linked lists of their own, and so on.
*   Return the list as a single level flattened doubly linked list
'''

from DLinkedList import Node, DLinkedList


def flattenList(linkedlist: DLinkedList) -> DLinkedList:

    prev = None
    current = linkedlist.head

    while current is not None:
        if (child := current.child) is not None:

            # Find last node of child list
            while child.next is not None:
                child = child.next

            # Link child and next
            if current.next is not None:
                child.next = current.next
                current.next.prev = child

            # Link current and child
            current.next = current.child
            current.child.prev = current

            current.child = None

        prev = current
        current = current.next

    linkedlist.tail = prev

    return linkedlist

# Time complexity: O(n)
# Space complexity: O(1)


# Test
linkedlist = DLinkedList().generateList(1, 7)
childList1 = DLinkedList().generateList(7, 10)
childList2 = DLinkedList().generateList(10, 12)
childList3 = DLinkedList().generateList(12, 14)
childList4 = DLinkedList().generateList(14, 17)

linkedlist.appendChildList(2, childList1)
linkedlist.appendChildList(8, childList2)
linkedlist.appendChildList(5, childList3)
linkedlist.appendChildList(6, childList4)

linkedlist.visualize()
flattenList(linkedlist).visualize()
