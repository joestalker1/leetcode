class Queue:
    def __init__(self, n):
        self.array_size = n
        self.head_array = [None] * n
        self.tail_array = [self.head_array]
        self.curr_array = 0

        self.head = 0
        self.tail = 0
        self.size = 0

    def enqueue(self, x):
        self.tail_array[self.curr_array][self.tail] = x

        if self.tail == self.array_size - 1:
            self.tail_array.append([None] * self.array_size)
            self.curr_array += 1

        self.tail = (self.tail + 1) % self.array_size
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            print('Cannot dequeue from empty queue.')
            return

        result = self.head_array[self.head]

        if self.head == self.array_size - 1:
            self.head_array = self.tail_array[1]
            self.tail_array = self.tail_array[1:]
            self.curr_array -= 1

        self.head = (self.head + 1) % self.array_size
        self.size -= 1

        return result

    def get_size(self):
        return self.size


q = Queue(3)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.dequeue()
q.dequeue()
