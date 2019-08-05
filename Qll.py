class Node:
    def __init__(self):
        self.data = None
        self.next = None

    def set_data(self,data):
        self.data = data

    def set_next(self, next):
        self.next = next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next 
    
    def has_next(self):
        return self.next!=None

class Queue:
    def __init__(self):
        self.size = 0
        self.front = None
        self.rear = None
    
    def enqueue(self,data):
        t = Node()
        t.set_data(data)
        t.set_next(None)
        if self.front==None:
            self.front = self.rear = t
        else:
            self.rear.set_next(t)
            self.rear = t
        self.size += 1
        self.print_list()
        
    def dequeue(self):
        if self.front == None:
            print("Nothing to delete")
            return
        else:
            t = self.front.get_data()
            t1 = self.front.get_next()
            self.front = t1
            if self.front == None:
                self.front = self.rear = None
            self.size -= 1
            self.print_list()

    def print_list(self):
        herelist = []
        if self.front == None:
            print("Queue is Empty")
        else:
            start = self.front
            while start != self.rear:
                t = start.get_data()
                herelist.append(t)
                start = start.get_next()
            t = start.get_data()
            herelist.append(t)
            print(herelist)

    def q_size(self):
        print("Size:",self.size)

    def get_front(self):
        if self.front ==  None:
            print("Queue is Empty")
        else:
            print("Front:",self.front.get_data())

    def get_rear(self):
        if self.rear ==  None:
            print("Queue is Empty")
        else:
            print("Rear:",self.rear.get_data())
    

myq = Queue()
myq.enqueue(4)
myq.enqueue(5)
myq.enqueue(6)
myq.q_size()
myq.get_front()
myq.get_rear()
myq.dequeue()
myq.dequeue()
myq.dequeue()
myq.q_size()
myq.enqueue(45)
myq.q_size()
myq.dequeue()