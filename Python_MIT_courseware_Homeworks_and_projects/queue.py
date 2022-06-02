class Queue(object):
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.insert(0, item)
    
    def dequeue(self):
        if(self.isEmpty() != True):
            print("Dequeueing...", self.queue[-1])
            return self.queue.pop()
        else:
            print("Queue is Empty!")
    
    def isEmpty(self):
        return self.queue == []

queue = Queue()
queue.enqueue(5)
queue.enqueue(6)
queue.dequeue()
queue.enqueue(7)
queue.dequeue()
queue.dequeue()
queue.dequeue()
