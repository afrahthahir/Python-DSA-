class Node:
    def __init__(self, data = None, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next

class doublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        currentHead = self.head
        newNode = Node(data,None,currentHead) #new node prev points to None, next points to current head
        if currentHead is not None: 
           currentHead.prev = newNode
        self.head = newNode
        
        

    def insert_at_end(self, data):
        

        if self.head is None:
            newNode = Node(data, None, None) 
            self.head = newNode
            return
        
        item = self.head
        while item:
            prevNode = item
            item = item.next
        newNode = Node(data,prevNode,None)
        prevNode.next = newNode


    def insert_at_middle(self, prevValue, data):
        occurence = 0
        item = self.head

        if item is None:
           self.head = Node(data, None, None)
           return
        
        if prevValue is None and occurence == 0:
            occurence += 1
            dl.insert_at_beginning(data)
    
        while item.next:
            prevNode = item
            nextNode = prevNode.next
            if prevNode.data == prevValue and occurence == 0:
               occurence += 1
               newNode = Node(data, prevNode, nextNode)
               prevNode.next = newNode
               break
            item = item.next

        if item.next is None and occurence == 0:
            occurence += 1
            dl.insert_at_end(data)

    def insert_values(self, dataList):
        self.head = None
        for item in dataList:
            dl.insert_at_end(item)


    def delete_at_beginning(self):

        currentHead = self.head
        if currentHead is None:
            print("list is empty")
            return
        nextNode = currentHead.next
        self.head = nextNode
        
    def delete_at_end(self):
        
        item = self.head

        if item is None:
            print("list is empty")
            return
        
        while item.next:
            prevNode = item
            item = item.next
        
        prevNode.next = None

    def delete_at_middle(self, key):

        occurence = 0
        item = self.head

        if item is None:
            print("list is empty")
            return
        
        if item.data == key and occurence == 0:
            occurence += 1
            dl.delete_at_beginning()

        
        while item.next:
            if item.data == key and occurence == 0:
                # print(item.data)
                prevNode = item.prev
                nextNode = item.next
                if prevNode and nextNode:
                    occurence += 1
                    prevNode.next = nextNode
                    nextNode.prev = prevNode
                    break
                
                    
                
            item = item.next

        if item.next is None and occurence == 0:
            occurence += 1
            dl.delete_at_end()

    def print_forward(self):

        item = self.head
        if item is None:
            print("list is empty")
            return
        
        dlstr = ""
        while item:
            dlstr += str(item.data) + "--->" 
            item = item.next

        print(dlstr)

    def print_backward(self):
        item = self.head
        if item is None:
            print("list is empty")
            return
        
        dlstr = ""
        while item.next:
            item = item.next

        while item:
            # print(item.data)
            dlstr +=  "<---" + str(item.data) 
            item = item.prev

        print(dlstr)

dl = doublyLinkedList()
dl.insert_at_beginning(10)
dl.insert_at_beginning(20)
dl.insert_at_beginning(30)
dl.insert_at_beginning(40)
dl.insert_at_beginning(50)
dl.insert_at_beginning(10)
dl.insert_at_end(60)
dl.insert_at_end(70)
dl.insert_at_middle(70,25)
# dl.delete_at_beginning()
# dl.delete_at_end()
# dl.delete_at_end()
dl.print_forward()
dl.delete_at_middle(40)
dl.delete_at_middle(25)
dl.delete_at_middle(10)
dl.insert_values(["apple", "mango", 10, 20, 30])
dl.print_forward()
dl.print_backward()

