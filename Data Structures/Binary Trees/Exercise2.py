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
          if data > self.data:
               if self.right:
                    self.right.add_child(data)
               else:
                    self.right = BTNode(data)

     def inorder_traversal(self):
          elements = []
          if self.left:
               elements += self.left.inorder_traversal()
          elements.append(self.data)
          if self.right:
               elements += self.right.inorder_traversal()
          return elements
     

     def find_min(self):
          if self.left is None:
               return self.data
          else:
               return self.left.find_min()
          

     def find_max(self):
          if self.right is None:
               return self.data
          else:
               return self.right.find_max()
          

     def deleteNodeByRightMinimum(self, value):

          #searching the value in left tree
          if value < self.data:
              self.left = self.left.deleteNodeByRightMinimum(value)

          #searching the value in right tree
          elif value > self.data:
               self.right = self.right.deleteNodeByRightMinimum(value)
          
          #value found
          else:
               #leaf node
               if self.left is None and self.right is None:
                    # Returning None will delete the node
                    return None
               
               # Node with right child
               elif self.left is None:
                    return self.right
               
               elif self.right is None:
                    return self.left
               
               #Node with two child (ie) Two approaches -> Take min from right subtree or take max from left subtree

               #Finding min value from right subtree, copying that min value in root node, deleting the min value node from right subtree
               min_value = self.right.find_min()
               self.data = min_value
               self.right = self.right.deleteNodeByRightMinimum(min_value)

          # To return the tree back after deleting
          return self
     


     def deleteNodeByLeftMaximum(self, value):

          #searching the value in left tree
          if value < self.data:
              self.left = self.left.deleteNodeByLeftMaximum(value)

          #searching the value in right tree
          elif value > self.data:
               self.right = self.right.deleteNodeByLeftMaximum(value)
          
          #value found
          else:
               #leaf node
               if self.left is None and self.right is None:
                    # Returning None will delete the node
                    return None
               
               # Node with right child
               elif self.left is None:
                    return self.right
               
               elif self.right is None:
                    return self.left
               
               #Node with two child (ie) Two approaches -> Take min from right subtree or take max from left subtree

               #Finding min value from right subtree, copying that min value in root node, deleting the min value node from right subtree
               max_value = self.left.find_max()
               self.data = max_value
               self.left = self.left.deleteNodeByLeftMaximum(max_value)

          # To return the tree back after deleting
          return self

     
def build_tree(elements):
     root = BTNode(elements[0])
     for i in range(1, len(elements)):
          root.add_child(elements[i])
     return root


if __name__ == "__main__":
     numbers = [17, 4, 1, 20, 9, 23, 18]
     number_tree = build_tree(numbers)
     print("Before: ", number_tree.inorder_traversal())

     #Leaf node deletion
     number_tree.deleteNodeByRightMinimum(1)
     print("After: ", number_tree.inorder_traversal())

     #node with two child deletion
     number_tree.deleteNodeByRightMinimum(20)
     print("After: ", number_tree.inorder_traversal())

     #node with one child deletion
     number_tree.deleteNodeByRightMinimum(9)
     print("After: ", number_tree.inorder_traversal())



     # #Leaf node deletion
     # number_tree.deleteNodeByLeftMaximum(1)
     # print("After: ", number_tree.inorder_traversal())

     # #node with two child deletion
     # number_tree.deleteNodeByLeftMaximum(20)
     # print("After: ", number_tree.inorder_traversal())

     # #node with one child deletion
     # number_tree.deleteNodeByLeftMaximum(9)
     # print("After: ", number_tree.inorder_traversal())
     

          