class Node:
	def __init__(self,value):
		self.value=value
		self.next=None

class SList:
	def __init__(self, value):
		node=Node(value)
		self.head = node

	def addNode(self, value):
		node=Node(value)
		runner=self.head
		while (runner.next !=None):
			runner= runner.next
		runner.next=node

	def removeNode(self,value):
		if self.value==value:
			self.head=self.head.next
		else if self.next=None:
			runner.next=None
		else
			self.head=self.head.next
			runner.next=runner.next.next


	def remove(self,value):
 		current = self.head;
 		previous = None;
		while current is not None:
  			if current.value == value:
    		# if this is the first node (head)
    			if previous is not None:
      				previous.nextNode = current.nextNode
    			else:
        			self.head = current.nextNode
  			previous = current
  			current = current.nextNode;

	def insert(self, value, index):
        node= Node(value, index)
        node.next = self.next
        self.next = node

	def printAllValues(self,msg=""):
		runner=self.head
		print("\n\nhead points to ", id(self.head))
        print("Printing the values in the list ---", msg,"---")
        while(runner.next != None):
            print(id(runner), runner.value, id(runner.next))
            runner = runner.next        
        print(id(runner), runner.value, id(runner.next))

list = SList(5)
list.addNode(7)
list.addNode(9)
list.addNode(1)
     
list.printAllValues("Attempt 1")