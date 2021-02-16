''' Question:
*   Given a limited list and numbers m and n, return it back with only
*   positions m to n in reverse
'''

from SLinkedList import Node, SLinkedList


def reversePortion2(linkedlist: SLinkedList, m: int, n: int) -> SLinkedList:

    position = 1
    start = None
    current = linkedlist.head

    # Store start node
    while position < m:
        start = current
        current = current.next
        position += 1

    end = current
    newList = None

    # Start reversing
    while position <= n:
        next_ = current.next
        current.next = newList
        newList = current
        current = next_
        position += 1

    # Attach head
    if start is not None:
        start.next = newList
    else:
        linkedlist.head = newList

    # Attach tail
    if current is not None:
        end.next = current
    else:
        linkedlist.tail = end

    return linkedlist

# Time complexity: O(n)
# Space complexity: O(1)


# Test
linkedlist = SLinkedList().generateList(length=7)

reversePortion2(linkedlist, 2, 6).listprint()
print(linkedlist.head.key)
print(linkedlist.tail.key)
