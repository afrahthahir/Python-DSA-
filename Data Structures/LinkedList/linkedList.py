
# Node class - node of the linked list
class Node: 
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

# Linkedlist class - init function -> whenever the linkedlist instance is called, a linked list is created with a head attribute value as None
class LinkedList: 
    def __init__(self):
        self.head = None


    def insert_at_beginning(self, data):
        newNode = Node(data,self.head)
        self.head = newNode
    

    def print(self):
        item = self.head

        if item is None:
            print("list is empty")
            return
        
        lls = ""
        while item:
            lls += str(item.data) + "--->" 
            item = item.next
            
        print(lls)


    def insert_at_end(self, data):
        

        if self.head is None:
            self.head = Node(data, None)
            return
       
        item = self.head
        
        while item.next:
            item = item.next
        
        newNode = Node(data, None)
        item.next = newNode

    def delete_at_beginning(self):
        item = self.head
        if item is None:
            print("list is empty")
            return
        self.head = item.next

    def delete_at_end(self):
        item = self.head
        if item is None:
            print("list is empty")
            return
        
        while item.next:
            prev = item
            item = item.next
        # print(prev.data)
        prev.next = None


    def delete_at_middle(self, key):
        occurance = 0
        item = self.head
        if item is None:
            print("list is empty")
            return
         
        if item.data == key:
            occurance += 1
            l.delete_at_beginning()

        if item.next is None:
            occurance += 1
            l.delete_at_end()

        while item.next:

            prev = item
            item = item.next
            if item.data == key and occurance == 0:
                occurance += 1
                prev.next = item.next
                break
            
        
    def insert_at_middle(self, prevNode, key):
        occurance = 0
        if self.head is None:
            self.head = Node(key,None)
            return

        item = self.head
        
        if prevNode is None:
            l.insert_at_beginning(key)
        
        # handles both insert at end and middle
        while item:
            prev = item
            if prev.data == prevNode and occurance == 0:
                occurance += 1
                newNode = Node(key, prev.next)
                prev.next = newNode
            item = item.next
        
        
        
    def insert_values(self, dataList):
        self.head = None
        
        for item in dataList:
            l.insert_at_end(item)



    

l = LinkedList()
l.insert_at_beginning(10)
l.insert_at_beginning(20)
# l.insert_at_beginning(10)
# l.insert_at_end(40)
# l.insert_at_end(50)
# l.insert_at_end(60)
# l.insert_at_end(70)
# # l.delete_at_beginning()
# # l.delete_at_beginning()
# # l.delete_at_end()
# # l.delete_at_middle(40)
# # l.delete_at_middle(30)
# l.insert_at_middle(10,25)
# l.delete_at_middle(10)
# l.insert_values(["banana","mango","grapes","orange"])
# l.print()
# l.insert_at_middle("mango","apple")
# l.print()
# l.delete_at_middle("orange")
# l.print()
# l.delete_at_middle("figs")
# l.print()
# l.delete_at_middle("banana")
# l.delete_at_middle("mango")
# l.delete_at_middle("apple")
# l.delete_at_middle("grapes")
l.delete_at_middle(10)
l.print()