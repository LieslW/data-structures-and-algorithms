from data_structures.stack import Stack, Node


class PseudoQueue:
    def __init__(self):
        self.inbox = Stack()
        self.outbox = Stack()

    def enqueue(self, value):
        self.inbox.push(value)

    def dequeue(self):
        while self.inbox.top:
            inbox_value = self.inbox.pop()
            self.outbox.push(inbox_value)

        if self.outbox.top:
            return_node = self.outbox.pop()
        while self.outbox.top:
            outbox_value = self.outbox.pop()
            self.inbox.push(outbox_value)

        return return_node
