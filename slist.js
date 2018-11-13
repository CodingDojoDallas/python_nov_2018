function Node(val){
    this.val = val
    this.next = null
}

function Slist(){
    this.head = null

    this.add = function(val){
        if(this.head == null){
            this.head = new Node(val)
            return this.head
        }
        runner = this.head
        while(runner.next!= null){
            runner = runner.next
        }
        runner.next = new Node(val)
        return this.head
    }

    this.display = function(runner){
        runner = this.head
        while(runner!=null){
            console.log(runner.val)
            runner=runner.next
        }
    }
    this.removefront = function(){
        this.head = this.head.next
    }

    this.getlength = function(){
        runner = this.head
        count = 0
        while(runner!=null){
            count += 1
            runner=runner.next
        }
        return count
    }

    this.remove = function(value){
        if (this.head.val == value){
            this.head = this.head.next
            return
        }
        runner = this.head
        while(runner.next!=null){
            if(runner.next.val == value){
                runner.next = runner.next.next
                return
            }
            runner = runner.next
        }
    }
}

list = new Slist()
list.add(27)
list.add(94)
list.add(200)
list.add(56)

length = list.getlength()
console.log("Length of the list is:", length)

console.log("\nElements of the list are")
list.display()

list.removefront()
console.log("\nElements of the list are")
list.display()

list.remove(56)
console.log("\nElements of the list are")
list.display()

list.remove(200)
console.log("\nElements of the list are")
list.display()

list.remove(94)
console.log("\nElements of the list are")
list.display()


//ptr is the reference to the first node
function add(ptr, val){
    if(ptr == null){
            ptr = new Node(val)
            return ptr
        }
        runner = ptr
        while(runner.next!= null){
            runner = runner.next
        }
        runner.next = new Node(val)
        return ptr
}

function display(ptr){
    runner = ptr
    while(runner!=null){
        console.log(runner.val)
        runner=runner.next
    }
}

function removefront(ptr){
    ptr = ptr.next
    return ptr
}

function getlength(ptr){
    runner = ptr
    count = 0
    while(runner!=null){
        count += 1
        runner=runner.next
    }
    return count

}

function remove(ptr, value){
    if (ptr.val == value){
        ptr = ptr.next
        return ptr
    }
    runner = ptr
    while(runner.next!=null){
        if(runner.next.val == value){
            runner.next = runner.next.next
            return ptr
        }
        runner = runner.next
    }
    return ptr
}

list2 = add(null, 5)
list2 = add(list2, 7)
list2 = add(list2, 9)
list2 = add(list2, 11)

console.log("\nList2 Elements:")
display(list2)

len=getlength(list2)
console.log("\nLength of list2:", len)

list2 = removefront(list2)
console.log("\nList2 Elements:")
display(list2)

list2 = remove(list2, 7)
console.log("\nList2 Elements:")
display(list2)

list2 = remove(list2, 9)
console.log("\nList2 Elements:")
display(list2)

list2 = remove(list2, 11)
console.log("\nList2 Elements:")
display(list2)