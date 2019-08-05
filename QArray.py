class Queue():
    def __init__(self,limit=5):
        self.que = []
        self.size = 0
        self.limit = limit
        self.front = None
        self.rear = None

    def enqueue(self,data):
        if self.size >= self.limit:
            print("Queue is full")
            return
        else:
            self.que.append(data)
            if self.front == None:
                self.front = self.rear = 0
            else:
                self.rear = self.size
            self.size += 1
        print("Queue after Enqueue:",self.que)

    def dequeue(self):
        if self.size <=0:
            print("Queue is Empty")
            return
        else:
            self.que.pop(0)
            self.size -= 1
            if self.size == 0:
                self.front = self.rear = None
            else:
                self.rear = self.size-1
        print("Queue after Dequeue:",self.que)
    
    def get_front(self):
        if self.front == None:
            print("Queue is empty")
            raise IndexError
        else:
            return self.que[self.front]

    def get_rear(self):
        if self.rear == None:
            print("Queue is empty")
            raise IndexError
        else:
            return self.que[self.rear]

    def q_size(self):
        print(self.size)


myq = Queue()
myq.enqueue(4)
myq.enqueue(5)
myq.enqueue(6)
myq.q_size()
myq.dequeue()
print(myq.get_front())
print(myq.get_rear())
myq.dequeue()
myq.dequeue()
myq.dequeue()
myq.q_size()