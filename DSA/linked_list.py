class Node:
    def __init__(self, value, prev=None , next=None):
        self.value = value
        self.prev = prev
        self.next = next

class Dll:
    def __init__(self,value=None):
        self.start = Node(value)
        print ( "created a linked list with initial value = ", self.start.value)
        if value == None:
            pass
        else:
            self.start.next = Node(value,self.start)

    def __move_till_last(self):
        ptr = self.start.next if self.start.next != None else self.start 

        while ptr.next != None:
            ptr = ptr.next

        return ptr
    
    def add_at_end(self,value):
        ptr = self.__move_till_last()
        ptr.next = Node(value)
    
    def add_at_i(self,value,i=-1):
        if i == -1:
            ptr = self.__move_till_last()
            ptr.next = Node(value)
            return
        else:
            ptr = self.start
            while i >= 0:
                ptr = ptr.next
                i -= 1
            ptr.next.next.prev


    def __repr__(self):
        ret_str = ""
        ptr = self.start.next if self.start.next != None else self.start

        if self.start.next == None:
            return "empty dll"

        while ptr.next != None:
            ret_str += " "+ str(ptr.value) + "->"
            ptr = ptr.next
        ret_str += " "+ str(ptr.value) + "->"

        return ret_str

x = Dll()
for i in range(9):
    x.add_at_end(i)

print(x)
        

