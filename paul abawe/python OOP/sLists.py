class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SList:
    def __init__(self, value):
        node = Node(value)
        self.head = node

    def addNode(self, value):
        node = Node(value)
        runner = self.head
        while(runner.next != None):
            runner = runner.next
        runner.next = node

    def printAllValues(self, msg=""):
        runner = self.head          # create a runner     
        print("\n\nhead points to ", id(self.head))
        print("Printing the values in the list ---", msg,"---")
        while(runner.next != None):
            print(id(runner), runner.value, id(runner.next))
            runner = runner.next
        print(id(runner), runner.value, id(runner.next))


    def removeNode(self, value):
        runner = self.head
        if runner and runner.value == value:
            self.head = runner.next
            runner = None
            return
        
        prev = None
        while(runner and runner.value != value):
            prev = runner
            runner = runner.next

        if runner is None:
            return

        prev.next = runner.next
        runner = None






print("\n\n\n\n================== START OF THE PROGRAM ================")       
list = SList(5)
list.addNode(7)
list.addNode(9)
list.addNode(1)
list.removeNode(5)
list.removeNode(9)


list.printAllValues("Attempt 1")