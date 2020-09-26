"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        currNode = self                                         # Start at top node
        while 1:                                                # Traverse infinitely until we return @ end of tree

            if value >= currNode.value:                         # Compare value w/ right
                if currNode.right:                              # Check if we reached end of tree
                    currNode = currNode.right                   # We didn't, traverse right, loop will run on new current ndoe
                else:
                    currNode.right = BSTNode(value)             # Add new leaf if found end of tree
                    return

            else:                                               # Same process if value <= left
                if currNode.left:
                    currNode = currNode.left
                else:
                    currNode.left = BSTNode(value)
                    return
                    

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        currNode = self
        while 1:
            if target > currNode.value:                 # Check if target is > current node value
                if currNode.right:                      
                    currNode = currNode.right           # Traverse right if .right exists
                else:
                    return False                        # Reached end of list, target not found

            elif target < currNode.value:               # Same process if target < current node value
                if currNode.left:
                    currNode = currNode.left
                else:
                    return False
            else:                                       # Target is equal to current node value, target found in list
                return True
