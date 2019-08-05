class Node:
    def __init__(self,data=None,next=None,prev=None):
        self.data = data
        self.next = next
        self.prev = prev

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

    def set_prev(self,prev):
        self.prev = prev 
    
    def get_prev(self):
        return self.prev

    def has_prev(self):
        return self.prev!=None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def insert_at_beginning(self,data):
        tnode = Node(data,None,None)
        if self.head == None:
            self.head = self.tail = tnode
        else:
            tnode.set_next(self.head)
            tnode.set_prev(None)
            self.head.set_prev(tnode)
            self.head = tnode
        self.length += 1

    def insert_at_end(self,data):
        tnode = Node(data,None,None)
        if self.head == None:
            self.head = self.tail = tnode
        else:
            tnode.set_prev(self.tail)
            tnode.set_next(None)
            self.tail.set_next(tnode) 
            self.tail = tnode 
        self.length += 1

    def insert_at_pos(self,pos,data): #Count of position start from Zero
        tnode = Node(data,None,None)
        if pos>self.length or pos<0:
            print ("Invalid Position to insert node")
        elif pos==0:
            self.insert_at_beginning(data)
        elif pos == self.length:
            self.insert_at_end(data)
        else:
            count=0
            current = self.head
            while count != pos:
                count = count + 1
                current = current.get_next()
            tnode.set_next(current)
            tnode.set_prev(current.get_prev())
            current.get_prev().set_next(tnode)
            current.set_prev(tnode)
            self.length += 1


    def delete_at_beginning(self):
        if self.length == 0:
            print ("Nothing to delete")
        else:
            current = self.head 
            current = current.get_next()
            current.set_prev(None)
            self.head = current
            self.length -= 1
        
    def delete_at_end(self):
        if self.length == 0:
            print ("Nothing to delete")
        else:
            current = self.tail
            current = current.get_prev()
            current.set_next(None)
            self.tail = current
            self.length -= 1

    def delete_at_pos(self,pos):
        current = self.head
        count = 0
        if pos > (self.length-1) or pos < 0: 
            print ("Position Invalid")
        elif self.length == 0:
            print ("List is Empty")
        elif pos==0:
            self.delete_at_beginning()
        elif pos == (self.length - 1):
            self.delete_at_end()
        else:
            while count != pos:
                current = current.get_next()
                count += 1
            current.get_prev().set_next(current.get_next())
            current.get_next().set_prev(current.get_prev())
            current.set_next(None)
            current.set_prev(None)
            self.length -= 1

    def delete_value(self,data):
        current = self.head
        if self.length == 0:
            print ("List is Empty")
        while current!=None:
            if current.get_data() == data:
                if self.length == 1:
                    self.head == None
                    self.tail == None
                    self.length -= 1
                elif current.get_prev() == None:
                    self.delete_at_beginning()
                elif current.get_next() == None:
                    self.delete_at_end()
                else:
                    current.get_prev().set_next(current.get_next())
                    current.get_next().set_prev(current.get_prev())
                    self.length -= 1
                return 
            current = current.get_next()
        print ("Element not found in list")





    def print_list(self):
        if self.length == 0:
            print ("List is Empty")
        else:
            current = self.head
            while current!=None:
                print (current.get_data())
                current = current.get_next()


def main():
    l1 = LinkedList()
    l1.insert_at_beginning(3)
    l1.insert_at_beginning(4)
    l1.insert_at_beginning(5)
    l1.insert_at_end(6)
    l1.insert_at_beginning(7)
    l1.insert_at_end(8)
    l1.insert_at_pos(5,45)
    l1.delete_at_end()
    l1.delete_at_pos(2)
    l1.delete_at_pos(4)
    l1.delete_value(6)
    l1.delete_at_beginning()
    l1.delete_at_end()
    l1.delete_value(5)
    l1.print_list()
if __name__ == "__main__":
    main()