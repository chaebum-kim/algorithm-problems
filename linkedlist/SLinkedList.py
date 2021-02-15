
class Node:
    def __init__(self, key=None):
        self.key = key
        self.next = None


class SLinkedList:
    def __init__(self, head: Node):
        self.head = head
        self.tail = head

    def append(self, node: Node):
        self.tail.next = node
        self.tail = self.tail.next

    def listprint(self):
        current = self.head
        while current is not None:
            print(current.key, end=" ")
            current = current.next
        print()
