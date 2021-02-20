''' Question:
*   Implement the class Queue using stacks. The queue methods you need to
*   implement are enuque, deque, peek, and empty.
'''


class QueueWithStacks:
    def __init__(self):
        self.stackIn = []
        self.stackOut = []

    def enque(self, value):
        self.stackIn.append(value)

    def deque(self):
        if not self.stackOut:
            while self.stackIn:
                self.stackOut.append(self.stackIn.pop())

        return self.stackOut.pop()

    def peek(self):
        if not self.stackOut:
            while self.stackIn:
                self.stackOut.append(self.stackIn.pop())

        return self.stackOut[len(self.stackOut)-1]

    def empty(self):
        if self.stackIn or self.stackOut:
            return False
        else:
            return True


if __name__ == '__main__':
    queue = QueueWithStacks()

    for num in range(1, 11):
        queue.enque(num)

    print(queue.peek())

    print(queue.deque())

    print(queue.empty())
