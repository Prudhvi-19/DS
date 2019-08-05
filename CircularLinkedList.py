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

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def list_length(self):
        current =self.head
        count = 1
        if self.head == None:
            return 0
        else:
            current = current.get_next()
            while current!=self.head:
                count += 1
                current = current.get_next()
            return count

    def display_list(self):
        current = self.head
        if self.length == 0:
            print ("List is Empty")
        else:
            print (current.get_data())
            current = current.get_next()
            while current != self.head:
                print (current.get_data())
                current = current.get_next()

    def insert_at_end(self,data):
        current = self.head
        tnode = Node()
        tnode.set_data(data)
        tnode.set_next(tnode)
        while current.get_next() != self.head:
            current = current.get_next()
        if self.head == None:
            self.head = tnode
        else:
            tnode.set_next(self.head)
            current.set_next(tnode)
        self.length += 1

    def insert_at_start(self,data):
        tnode = Node()
        tnode.set_data(data)
        tnode.set_next(tnode)
        if self.head == None:
            self.head = tnode
        else:
            tnode.set_next(self.head)
            current = self.head
            while current.get_next() != self.head:
                current = current.get_next()
            current.set_next(tnode)
            self.head = tnode
        self.length += 1

    def delete_at_start(self):
        current = self.head
        if self.head == None:
            print ("Empty List")
        elif self.length == 1:
            self.head = None
            self.length -= 1
        else:
            while current.get_next()!=self.head:
                current = current.get_next()
            current.set_next(self.head.get_next())
            self.head = self.head.get_next()
            self.length -= 1

    def delete_at_end(self):
        current = self.head
        previous = self.head
        if self.head == None:
            print ("List Empty")
        elif self.length == 1:
            self.head = None
            self.length -= 1
        else:
            while current.get_next() != self.head:
                previous = current
                current = current.get_next()
            previous.set_next(current.get_next())
            self.length -= 1

def main():
    a = 0
    l1 = LinkedList()
    l1.insert_at_start(3)
    l1.insert_at_start(4)
    l1.insert_at_start(5)
    l1.insert_at_end(6)
    l1.insert_at_start(7)
    l1.insert_at_end(8)
    a += 1
    print ("Here %d"%a)
    l1.display_list()
    l1.delete_at_start()
    l1.delete_at_end()
    a += 1
    print ("Here %d"%a)
    l1.display_list()
    l1.delete_at_start()
    l1.delete_at_end()
    a += 1
    print ("Here %d"%a)
    l1.display_list()
    l1.delete_at_start()
    l1.delete_at_end()
    a += 1
    print ("Here %d"%a)
    l1.display_list()
    l1.insert_at_start(45)
    l1.insert_at_end(46)
    l1.insert_at_start(47)
    l1.insert_at_end(48)
    a += 1
    print ("Here %d"%a)
    l1.display_list()
   
if __name__ == "__main__":
    main()




        