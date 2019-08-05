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

class Stack():
    def __init__(self,data=None):
        self.head = None
        if data:
            self.push(data)
    
    def push(self,in1):
        temp = Node()
        temp.set_data(in1)
        temp.set_next(self.head)
        self.head = temp

    def pop(self):
        if self.head == None:
            print("Stack Underflow")
        else:
            temp = self.head.get_data()
            self.head = self.head.get_next()
            return temp

    def peep(self):
        if self.head == None:
            print("Stack Underflow")
        else:
            return self.head.get_data()

    def print_stack(self):
        temp = self.head
        a = []
        while temp!=None:
            a.append(temp.get_data())
            temp = temp.get_next()
        print(a)


my_stack = Stack()
my_stack.push(45)
my_stack.print_stack()
my_stack.push(46)
my_stack.push(47)
my_stack.print_stack()
my_stack.push(48)
my_stack.print_stack()
a=my_stack.peep()
print(a)
a=my_stack.pop()
print(a)
a=my_stack.pop()
print(a)
a=my_stack.pop()
print(a)
a=my_stack.pop()
print(a)
a=my_stack.pop()
print(a)