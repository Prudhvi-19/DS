class Stack():
    def __init__(self,limit=10):
        self.stk = []
        self.limit = limit
    
    def is_empty(self):
        return len(self.stk)<=0

    def push(self,data):
        if len(self.stk)>=self.limit:
            self.resize()
        self.stk.append(data)
        print("Stack: ",self.stk)

    def pop(self):
        if len(self.stk)<=0:
            print("Stack Underflow")
        else:
            return self.stk.pop()

    def peep(self):
        if len(self.stk)<=0:
            print("Nothing to Peep")
        else:
            return self.stk[-1]

    def size(self):
        return len(self.stk)

    def resize(self):
        newStk = list(self.stk)
        self.limit = 2*self.limit
        self.stk = newStk
    
my_stack = Stack(3)
my_stack.push(45)
my_stack.push(46)
a=my_stack.size()
print(a)
my_stack.push(47)
my_stack.push(48)
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