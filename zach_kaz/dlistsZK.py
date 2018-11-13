class Node:
    def __init__(self,value,name):
        self.value=value
        self.name=name
        self.next=None
        self.previous=None

class dList:
    def __init__(self,value,name):
        node=Node(value,name)
        self.head=node
    
    def addNode(self,value,name):
        node=Node(value,name)
        runner=self.head
        while (runner.next!=None):
            runner=runner.next
        runner.next=node
        node.previous=runner
    
    def removeNode(self,finder):
        x=self.head
        if x.value==finder:
            self.head=x.next
        while (x.next!=None):
            if(x.next.value==finder):
                if(x.next.next==None):
                    x.next=None
                else:
                    x.next=x.next.next
                    x.next.next.previous=x
            x=x.next
            
    def insertNode(self,value,name,index):
        x=self.head
        if 0==index:
            node=Node(value,name)
            x.previous=node
            node.next=x
            self.head=node
            return self
        y=0
        while y<index:
            if (y+1==index):
                node=Node(value,name)
                node.previous=x
                if (x.next!=None):
                    node.next=x.next
                x.next=node
                return self
            if (x.next==None):
                node=Node(value,name)
                x.next=node
                node.previous=x
                return self
            y+=1
            x=x.next
            


phish=dList(1,"Wayne")
phish.addNode(50,"Joshua")
phish.addNode(345,"AWOOGA")
phish.addNode(876,"Jarule")
print(phish.head.name)
print(phish.head.next.name)
#print(phish.head.next.previous.name)
print(phish.head.next.next.name)
print(phish.head.next.next.next.name)
#print(phish.head.next.next.next.next.name)
#phish.removeNode(50)
phish.insertNode(34,"Crane",100)
print(phish.head.name)
print(phish.head.next.name)
#print(phish.head.next.previous.name)
print(phish.head.next.next.name)
print(phish.head.next.next.next.name)
print(phish.head.next.next.next.next.name)

