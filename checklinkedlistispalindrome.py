class Node: 
    def __init__(self, value): 
        self.data = value 
        self.next = None
        
class LinkedList: 
  
    def __init__(self): 
        self.head = None
  
    def push(self, new_value): 
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node 
          
    def isPalin(self):
        if  self.head==None:
            return False
        if self.head.next==None:
            return True
        temp=self.head
        lst=[]
        while temp!=None:
            lst.append(temp.data)
            temp=temp.next
        if lst==lst[::-1]:
            return True
        else:
            return False

def read_list_input():
    vals = input().split(' ')
    linkedList = LinkedList() 
    for val in vals:
        linkedList.push(val)
    return linkedList

test_cases = int(input())
for i in range(test_cases):
    linkedList = read_list_input()
    print(linkedList.isPalin())
