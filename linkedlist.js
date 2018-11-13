//class Node
function Node(value){
	this.val = value
	this.next = null
}

//class Linkedlist
function BigNode(){
	this.head = null

	//displays the values in the linked list
	this.show = function(){
		var runner = this.head
		while(runner!=null){
			console.log(runner.val)
			runner = runner.next
		}
	}

	this.copy = function(linkedlist /* List which has the nodes with values: 7, 8, 89 */){
		var pointer = linkedlist.head //Node with value 7
		var newlist2 = new BigNode() //new  empty list
		if(pointer == null){
			return newlist2
		}
		newlist2.head = new Node(pointer.val)
		var runner = newlist2.head
		while(pointer.next!=null){
			runner.next = new Node(pointer.next.val)
			//console.log("*****",runner.next.val)
			pointer = pointer.next
			runner = runner.next

		}
		//newlist2.show() -- to debug
		return newlist2 //returns back a new linkedlist with the values : 7, 8, 89
	}
}


//we can also create an add node funtion as a substit-ute
node1 = new Node(7)
node2 = new Node(9)
node3 = new Node(10)
node4 = new Node(11)
node1.next = node2
node2.next = node3
node3.next = node4

list = new BigNode()
list.head = node1
list.show()

newlist = list.copy(list)
newlist.show()



