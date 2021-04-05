''' Question:
*   Implement the class Queue using stacks. The queue methods you need to
*   implement are enuque, deque, peek, and empty.
'''


class QueueWithStacks:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def enque(self, value):
        self.stack_in.append(value)

    def deque(self):
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())

        return self.stack_out.pop()

    def peek(self):
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())

        return self.stack_out[len(self.stack_out)-1]

    def empty(self):
        if self.stack_in or self.stack_out:
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
