# Python program to detect loop in the linked list 

# Node class 
class Node: 

	# Constructor to initialize the node object 
	def __init__(self, data): 
		self.data = data 
		self.next = None

class LinkedList:
# Function to initialize head 
    def __init__(self): 
        self.head = None

# Do not change anything above this line
    def deleteNode(self, position): 
        # YOU ONLY NEED TO COMPLETE THIS FUNCTION.
        if position==0:
            temp=self.head
            self.head=temp.next
            return
        temp=self.head
        while(position>1 and temp.next!=None):
            temp=temp.next
            position-=1
        if temp.next==None:
            temp=None
            return
        temp.next=temp.next.next
  
    # Utility function to print the linked LinkedList 
    def printList(self): 
        temp = self.head 
        while(temp): 
            print(temp.data, end=" ")
            temp = temp.next


# Do not change anything below this line
if __name__ == '__main__':
    
    n = int(input())

    # Start with the empty list 
    llist = LinkedList() 

    temp = [int(x) for x in input().split()]

    if(n<1):
        llist.head = None
    elif(n<2):
        llist.head = Node(temp[0])
    else:
        llist.head = Node(temp[0])
        second = Node(temp[1])
        llist.head.next = second
        curr = llist.head.next


    for i in range(2,n):
        t = Node(temp[i])
        curr.next = t
        curr = curr.next

    pos = int(input())

    llist.deleteNode(pos)
    llist.printList()
