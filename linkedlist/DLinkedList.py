from __future__ import annotations


class Node:
    def __init__(self, key=None):
        self.key = key
        self.prev = None
        self.next = None
        self.child = None


class DLinkedList:
    def __init__(self, head=None):
        self.head = head
        self.tail = head

    def append(self, node: Node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = self.tail.next

    def appendChildList(self, parentKey, childList: DLinkedList):
        def findKey(node: Node, parentKey):
            if node is not None:
                if node.key == parentKey:
                    return node

                child = node.child
                if (ret := findKey(child, parentKey)) is not None:
                    return ret

                next_ = node.next
                if (ret := findKey(next_, parentKey)) is not None:
                    return ret

        parent = findKey(self.head, parentKey)
        parent.child = childList.head

    def generateList(self, start: int, end: int):

        for num in range(start, end):
            node = Node(num)
            self.append(node)

        return self

    def listprint(self):
        current = self.head
        while current is not None:
            print(current.key, end=" ")
            current = current.next
        print("")

    def visualize(self):
        def visualizeNode(node: Node, index=0):

            if node is not None:
                print(node.key, end="")

                if node.next is not None:
                    print("---", end="")

                visualizeNode(node.next, index+1)

                if node.child is not None:
                    print(f"\n" + ("    "*index) + "|")
                    print(("    "*index), end="")

                visualizeNode(node.child, index)

        visualizeNode(self.head)
        print()
