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

    def countPairs(self, head2, x):
        # YOU ONLY NEED TO COMPLETE THIS FUNCTION.
        dict={}
        count=0
        temp2=head2
        while temp2!=None:
            dict[temp2.data]=1
            temp2=temp2.next
        temp1=self.head
        while temp1!=None:
            if (x-temp1.data) in dict:
                count+=1
            temp1=temp1.next
        return count
        


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

    # For 2nd linked list:
    m = int(input())

    # Start with the empty list 
    llist2 = LinkedList() 

    temp = [int(x) for x in input().split()]

    if(m<1):
        llist2.head = None
    elif(m<2):
        llist2.head = Node(temp[0])
    else:
        llist2.head = Node(temp[0])
        second = Node(temp[1])
        llist2.head.next = second
        curr = llist2.head.next


    for i in range(2,m):
        t = Node(temp[i])
        curr.next = t
        curr = curr.next

    print(llist.countPairs(llist2.head, int(input())))
