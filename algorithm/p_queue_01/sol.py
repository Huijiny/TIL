class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, elem):
        self.data.append(elem)

    def dequeue(self):
        return self.data.pop(0)

    def is_empty(self):
        return not bool(len(self.data))

    def get_front(self):
        return self.data[0]

    def get_rear(self):
        return self.data[-1]

q = Queue()
print(q.enqueue(1), q.data)
print(q.enqueue(2), q.data)
print(q.get_front())
print(q.get_rear())
print(q.dequeue(), q.data)
print(q.dequeue(), q.data)

