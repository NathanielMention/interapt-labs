class Queue:
    # Create an empty list to model the queue data
    def __init__(self):
        self._queue_data = []

    # Return True if queue is empty, False otherwise
    def is_empty(self):
        return len(self._queue_data) == 0

    # Add an element to the end (tail) of the queue
    def enqueue(self, value):
        self._queue_data.append(value)

    # Return a reasonable string representation of a queue
    def __str__(self):
        return f'Queue Data: {self._queue_data}'

    # Remove and return the first (head) of the queue (LBYL)
    def dequeue(self):
        # AttributeError: 'list' object has no attribute 'is_empty'
        # len(self._queue_data) == 0
        if self.is_empty():
            print("Queue is empty - can't deque element")
            # return None
        else:
            return self._queue_data.pop(0)
        #
        # head = self._queue_data.pop(0)
        # return head

    # Return the number of elements in the queue
    def size(self):
        return len(self._queue_data)

    # Return the first (head), but do not remove it (EAFP)
    def peek(self):
        try:
            return self._queue_data[0]
        except Exception as exc:
            print(f"Exception when peeking: {exc}")


if __name__ == '__main__':
    q = Queue()          # Initially, queue object is empty
    print(q.is_empty())
    # q.enqueue('First')   # Add to back of the queue
    # q.enqueue('Second')  # Ditto
    print(q)              # Queue Data:

    # Remove and return the first (head) of the queue
    print(f'Queue head: {q.dequeue()}')
    print(f'Now, the queue looks like: {q}')

    print(q.size())
    print(q.peek())      # Return the first (head), but do not remove it
    print(f'Now, the queue looks like: {q}')
