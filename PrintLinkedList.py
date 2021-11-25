class Node:
    def __init__(self, key):
        self.data = key                         #self.data=1
        self.next = None                        #self.next=None


class LL:
    def __init__(self):
        self.head = None
        
#complete the Display function given below
    def display(self):
        temp=self.head
        print("head",end="->")
        while temp!=None:
           print(temp.data,end="->")
           temp=temp.next
        print(None)
    @staticmethod
    def insert_node(val, current):              #insert_node(2,1):
        temp = Node(val)                        #temp=Node(2)=2
        current.next = temp                     #head.next=Node(2)
        current = current.next                  #current=head.next
        return current                          #return head.next


ll = LL()
num = [int(i) for i in input().split("->")]     #[1,2,3,4]
ll.head = Node(num[0])                          #ll.head=1
curr = ll.head                                  #curr=1
for i in num[1:]:                               #[2,3,4]
    curr = LL.insert_node(i, curr)              #curr=LL.insert_node(2,1)
ll.display()
