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
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.get_next()
        return count

    def insert_at_beginning(self,data):
        tnode = Node()
        tnode.set_data(data)
        if self.length == 0:
            self.head = tnode
        else:
            tnode.set_next(self.head)
            self.head = tnode
        self.length += 1

    def insert_at_end(self,data):
        tnode = Node()
        tnode.set_data(data)
        current = self.head

        while current.get_next() != None:
            current = current.get_next()

        current.set_next(tnode)
        self.length += 1

    def insert_at_pos(self,pos,data):
        if pos > self.length or pos < 0:
            return None
        else:
            if pos==0:
                self.insert_at_beginning(data)
            else:
                if self.length == pos:
                    self.insert_at_end(data)
                else:
                    tnode = Node()
                    tnode.set_data(data)
                    count = 1
                    current = self.head
                    while count < pos-1:
                        count+=1
                        current = current.get_next()
                    tnode.set_next(current.get_next())
                    current.set_next(tnode)
                    self.length += 1

    def delete_from_beginning(self):
        if self.length == 0:
            print ("The List is Empty")
        else:
            self.head = self.head.get_next()
            self.length -= 1

    def delete_from_end(self):
        if self.length == 0:
            print ("The list is Empty")
        else:
            if self.length == 1:
                self.head = None
            else:
                current = self.head
                while current.get_next().get_next() != None:
                    current = current.get_next()
                current.set_next(None)
            self.length -= 1

    def delete_value(self,data):
        current = self.head
        previous = self.head

        while current.get_next()!=None:
            if current.get_data() == data:
                previous.set_next(current.get_next())
                self.length -= 1
                return
            else:
                previous = current
                current = current.get_next()
        if current.get_next() == None and current.get_data() == data:
            previous.set_next(None)
            self.length -= 1
            return
        print ("The Value doesnt exist")

    def delete_at_pos(self,pos):
        count = 0
        current = self.head
        previous = self.head
        if pos > self.length or pos < 1:  #counting First Node as position 1
            print ("Invalid Position to delete from")
        else:
            if pos == 1:
                self.delete_from_beginning()
            else:
                if pos == self.length:
                    self.delete_from_end()
                else:
                    while count<pos or current.get_next() == None:
                        count += 1
                        if count == pos:
                            previous.set_next(current.get_next())
                            self.length -= 1
                            return
                        else:
                            previous = current
                            current = current.get_next()
                   
    
    def delete_list(self):
        self.head = None

        
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
    l1.insert_at_pos(1,10)
    l1.insert_at_end(6)
    a = l1.list_length()
    print ("Count : %d" % a)
    l1.print_list()
    print ("New Line")

    l1.delete_at_pos(5)
    a = l1.list_length()
    print ("Count : %d" % a)
    l1.print_list()
    print ("New Line")
    l1.delete_value(10)
    a = l1.list_length()
    print ("Count : %d" % a)
    l1.print_list()
    print ("New Line")
    l1.delete_from_beginning()
    l1.delete_from_end()
    a = l1.list_length()
    print ("Count : %d" % a)
    l1.print_list()
    l1.delete_from_end()
    a = l1.list_length()
    print ("Count : %d" % a)
    l1.print_list()

if __name__ == "__main__":
    main()