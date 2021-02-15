''' Question:
*   Given a linked list, return it in reverse
'''
from SLinkedList import Node, SLinkedList


def reverseLinkedList(linkedlist: SLinkedList) -> SLinkedList:

    prev = None
    current = linkedlist.head

    while current is not None:
        next_ = current.next
        current.next = prev
        prev = current
        current = next_

    temp = linkedlist.head
    linkedlist.head = linkedlist.tail
    linkedlist.tail = temp

    return linkedlist

# Time complexity: O(n)
# Space complexity: O()


# Test
node = Node(key=1)
linkedlist = SLinkedList(head=node)

node = Node(key=2)
linkedlist.append(node=node)

node = Node(key=3)
linkedlist.append(node=node)

node = Node(key=4)
linkedlist.append(node=node)

node = Node(key=5)
linkedlist.append(node=node)

reverseLinkedList(linkedlist).listprint()
