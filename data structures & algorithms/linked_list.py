class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        node =  Node(value)
        self.head = node
        self.tail = node
        self.length = 1
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(f"Value: {temp.value}")
            temp = temp.next
        
        print(f"Length of list: {self.length}")
    
    def append(self,value):
        node = Node(value)
        temp = self.tail
        temp.next = node
        self.tail = node
        self.length += 1
    
    def pop(self):
        if self.length == 0:
            print("Nothing to pop!!!")
            return None
        elif self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
        else:
            temp = self.head
            
            while (temp.next):
                prev = temp
                temp = temp.next
            
            self.tail = prev
            prev.next = None
        
        self.length -= 1
        #print(f"Tail: {self.tail.value}")
        return temp.value
    
    def prepend(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        self.length += 1

    def pop_first(self):
        if self.length == 0:
            print("Nothing to pop!!!")
            return None
        elif self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None

        self.length -= 1
        return temp.value


        

my_ll = LinkedList(25)
print(f"Head: {my_ll.head.value}")
my_ll.append(36)
my_ll.append(49)
my_ll.append(64)
my_ll.append(81)
my_ll.print_list()
print(my_ll.pop())
print(my_ll.pop())
#print(my_ll.pop())
my_ll.prepend(121)
my_ll.prepend(144)
my_ll.print_list()
my_ll.pop_first()
print(my_ll.pop())
print(my_ll.pop())
my_ll.pop_first()
my_ll.print_list()
print(my_ll.pop())
my_ll.print_list()
my_ll.pop_first()
