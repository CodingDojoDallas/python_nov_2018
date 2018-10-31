class Node:
    def __init__(self,value,name):
        self.value=value
        self.next=None
        self.name=name

class sList:
    def __init__(self,value,name):
        node=Node(value,name)
        self.head=node

    def addNode(self,value,name):
        node=Node(value,name)
        runner=self.head
        while (runner.next !=None):
            runner=runner.next
        runner.next=node
    
    def removeNode(self,finder):
        x=self.head
        if x.value==finder:
            self.head=x.next
        while (x.next!=None):
            if x.next.value==finder:
                if (x.next.next==None):
                    x.next=None
                    continue
                else:
                    x.next=x.next.next
            x=x.next
    
    def insertNode(self,value,name,index):
        spot=self.head
        if (index==0):
            node=Node(value,name)
            node.next=spot
            self.head=node
        x=0
        while x<index:
            if (x+1==index):
                node=Node(value,name)
                if (spot.next!=None):
                    node.next=spot.next
                spot.next=node
                return self
            if (spot.next==None):
                node=Node(value,name)
                spot.next=node
                return self
            spot=spot.next
            x+=1



listicle=sList(4,"Jim")
listicle.addNode(10,"James")
#print(listicle.head.next.name)
listicle.addNode(15,"Jason")
listicle.addNode(3049,"Josh")
listicle.addNode(1111,"Juan")
#listicle.removeNode(15)
print(listicle.head.name)
print(listicle.head.next.name)
print(listicle.head.next.next.name)
print(listicle.head.next.next.next.name)
print(listicle.head.next.next.next.next.name)
listicle.insertNode(230,"JEFFREY!",100)
print(listicle.head.name)
print(listicle.head.next.name)
print(listicle.head.next.next.name)
print(listicle.head.next.next.next.name)
print(listicle.head.next.next.next.next.name)
print(listicle.head.next.next.next.next.next.name)

