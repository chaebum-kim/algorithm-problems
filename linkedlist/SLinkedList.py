
class Node:
    def __init__(self, key=None):
        self.key = key
        self.next = None


class SLinkedList:
    def __init__(self, head=None):
        self.head = head
        self.tail = head

    def append(self, node: Node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next

        return self.tail

    def generateList(self, length: int):
        for number in range(1, length+1):
            node = Node(key=number)
            self.append(node)

        return self

    def getNode(self, key):
        current = self.head
        while current is not None:
            if current.key == key:
                return current
            current = current.next
        return None

    def listprint(self):
        current = self.head
        while current is not None:
            print(current.key, end=" ")
            current = current.next
        print()
