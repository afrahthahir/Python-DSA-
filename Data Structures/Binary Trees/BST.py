class BTNode: 

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):

        # Duplicate values not allowed in Binary Tree, so it is used to implement Sets in python
        #  (ie) Set use Binary tree internally to avoid duplicate
        if data == self.data:
            # print(self.data)
            return
        
        # Value passed is < our existing data, so it should be inserted in left tree
        if data < self.data:
        #    print(self.data)
           # There is a left node exists, so adding a child inside the left tree
           if self.left:
             
             self.left.add_child(data)

           # No left node is present so creating a new node on left
           else:

             self.left = BTNode(data)  
        
        #Value passed is > our existing data, so it should be inserted in right tree
        else:
            
            # There is a right node exists, so adding a child inside the right tree
            if self.right:
               
               self.right.add_child(data)
            
            #No right node is present so creating a new node on right
            else:
               
               self.right = BTNode(data)


    def search(self, value):
       
       if value == self.data:
          return True
       #left tree
       if value < self.data:
          if self.left:
            return self.left.search(value)
          else:
             return False
       #right tree
       if value > self.data:
          if self.right:
            return self.right.search(value)
          else:
             return False
       


    def inorder_traversal(self):
       
       elements = []

       #visit left tree
       if self.left:
          elements += self.left.inorder_traversal()

       #visit base node
       elements.append(self.data)

       #visit right tree    
       if self.right:
          elements += self.right.inorder_traversal()
       
       return elements

   



def build_tree(numbers):
   
   root = BTNode(numbers[0])
   for i in range(1, len(numbers)):   
      root.add_child(numbers[i])
    #   print(i)
   return root

if __name__ == "__main__":
    number_tree = [54, 32, 43, 1, 34, 90, 78, 89]
    binaryTree = build_tree(number_tree)
    print(binaryTree.inorder_traversal())
    print(binaryTree.search(90))
    
                   

# Adding child logic

# 54 - root
# 32 -> add_child(32) ->
# 32 < 54 = True , so left tree
# there is no left child for 54, so creating 32 as a left node -> 54 left node = 32
# 43 -> add_child(43) ->
# 43 < 54 = True, so left tree
# there is already 32 in left of 54, so add_child(43) to left node 32, now self.data = 32
# 43 > 32 = True, so right tree
# there is no right child for 32, so creating 43 as a right node -> 32 right node = 43
# 1 -> add_child(1) -> 
# 1 < 32 = True, so left tree
# there is no left child for 32, so creating 1 as a left node -> 32 left node = 1

# At the end, this is the tree
#     54
#    /  \
#   32   90
#  /  \   /
# 1    43 78
#     /     \
#    34      89


# Inorder traversal logic (Left, Root, Right)
# Step 1: Start at the Root (54)
# Visit left subtree (32) first.

# Call: inorder_traversal(32)

# Step 2: Process Left Subtree (32)
# Visit left subtree (1) first.

# Call: inorder_traversal(1)

# Step 3: Process Leftmost Node (1)
# Left subtree is None, so return [1]

# Visit Node 1 → Add 1 to the list.

# Right subtree is None, return [1] back to 32.

# Result so far: [1]

# Step 4: Back to Node (32)
# Visit Node 32 → Add 32 to the list.

# Visit Right Subtree (43)

# Call: inorder_traversal(43)

# Step 5: Process Right Subtree (43)
# Visit left subtree (34) first.

# Call: inorder_traversal(34)

# Step 6: Process Leftmost Node (34)
# Left subtree is None, return [34].

# Visit Node 34 → Add 34 to the list.

# Right subtree is None, return [34] back to 43.

# Result so far: [1, 32, 34]

# Step 7: Back to Node (43)
# Visit Node 43 → Add 43 to the list.

# Right subtree is None, return [1, 32, 34, 43] back to 54.

# Result so far: [1, 32, 34, 43]

# Step 8: Back to Root (54)
# Visit Node 54 → Add 54 to the list.

# Visit Right Subtree (90)

# Call: inorder_traversal(90)

# Step 9: Process Right Subtree (90)
# Visit left subtree (78) first.

# Call: inorder_traversal(78)

# Step 10: Process Left Subtree (78)
# Left subtree is None, so process node 78.

# Visit Node 78 → Add 78 to the list.

# Visit Right Subtree (89)

# Call: inorder_traversal(89)

# Step 11: Process Rightmost Node (89)
# Left subtree is None, return [89].

# Visit Node 89 → Add 89 to the list.

# Right subtree is None, return [89] back to 78.

# Result so far: [1, 32, 34, 43, 54, 78, 89]

# Step 12: Back to Node (90)
# Visit Node 90 → Add 90 to the list.

# Right subtree is None, return [1, 32, 34, 43, 54, 78, 89, 90]