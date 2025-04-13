class BTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):

        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BTNode(data)

        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BTNode(data)


    #leftmost node in the left tree from the root node is your min element
    def find_min(self):

        if self.left is None:
            return self.data
        else:
            return self.left.find_min()
    
    #rightmost node in the right tree from the root node is your max element
    def find_max(self):

        if self.right is None:
            return self.data
        else:
            return self.right.find_max() 


    def calculate_sum(self):

        sum = self.data

        if self.left: 
            sum += self.left.calculate_sum()

        if self.right: 
            sum += self.right.calculate_sum()

        return sum
    
    def post_order_traversal(self): # Left, right, root

        elements = []
        
        # visit left node
        if self.left: 
            elements += self.left.post_order_traversal()
        
        #visit right node
        if self.right:
            elements += self.right.post_order_traversal()

        #visit base node
        elements.append(self.data)
        
        return elements
    

    def pre_order_traversal(self): # root, Left, right

        elements = []

        #visit base node
        elements.append(self.data)
        
        # visit left node
        if self.left: 
            elements += self.left.pre_order_traversal()
        
        #visit right node
        if self.right:
            elements += self.right.pre_order_traversal()

        
        return elements



def build_tree(elements):
    root = BTNode(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root




if __name__ == "__main__":
    numbers = [54, 32, 43, 34, 23, 45, 19, 10, 190, 78, 89, 98, 120, -430]
    numbers_tree = build_tree(numbers)
    minNumber = numbers_tree.find_min()
    maxNumber = numbers_tree.find_max()
    totalSum = numbers_tree.calculate_sum()
    print("Minimum element of the binary tree",minNumber)
    print("Maximum element of the binary tree",maxNumber)
    print("Sum of the total binary tree", totalSum)
    print("Post order traversal", numbers_tree.post_order_traversal())
    print("Pre order traversal", numbers_tree.pre_order_traversal())
