import math


class PriorityQueue:

    def __init__(self, comparator=lambda a, b: a > b):
        self.__heap = []
        self.__comparator = comparator

    def size(self):
        return len(self.__heap)

    def is_empty(self):
        return not bool(self.__heap)

    def peek(self):
        return self.__heap[0]

    def __parent(self, index):
        return math.floor((index-1)/2)

    def __left_child(self, index):
        return index * 2 + 1

    def __right_child(self, index):
        return index * 2 + 2

    def __compare(self, i, j):
        return self.__comparator(self.__heap[i], self.__heap[j])

    def __swap(self, i, j):
        self.__heap[i], self.__heap[j] = self.__heap[j], self.__heap[i]

    def push(self, value):
        self.__heap.append(value)
        self.__sift_up()
        return self.size()

    def __sift_up(self):
        index = self.size() - 1
        while (parent := self.__parent(index)) >= 0 and self.__compare(index, parent):
            self.__swap(parent, index)
            index = parent

    def pop(self):
        if self.size() > 1:
            self.__swap(0, self.size()-1)
        popped_value = self.__heap.pop()
        self.__sift_down()
        return popped_value

    def __sift_down(self):
        index = 0
        size = self.size()

        while self.__left_child(index) < size or self.__right_child(index) < size:
            left_child = self.__left_child(index)
            right_child = self.__right_child(index)

            if right_child < size:
                if self.__compare(left_child, right_child):
                    greater_child = left_child
                else:
                    greater_child = right_child
            else:
                greater_child = left_child

            if self.__compare(greater_child, index):
                self.__swap(index, greater_child)
                index = greater_child
            else:
                break

    def queue_print(self):
        print(self.__heap)


if __name__ == '__main__':
    priority_queue = PriorityQueue()

    for num in range(10, 56, 5):
        priority_queue.push(num)
    priority_queue.queue_print()

    for i in range(10):
        print(priority_queue.pop())
    priority_queue.queue_print()
