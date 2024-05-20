class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


    def traverse_pre_order(self):
        print(f"{self.val}-->", end=" ")    # Visit the root node
        if self.left:   # Visit all nodes of left subtree
            self.left.traverse_pre_order()
        if self.right:  # Visit all the nodes of the right subtree
            self.right.traverse_pre_order()

    def traverse_in_order(self):
        if self.left:   # Visit all nodes of the left subtree
            self.left.traverse_in_order()
        print(f"{self.val}-->", end=" ")    # Visit the root node
        if self.right:  # Visit the nodes of the right subtree
            self.right.traverse_in_order()

    def traverse_post_order(self):
        if self.left:   # visit all the nodes of left subtree
            self.left.traverse_post_order()
        if self.right:  # visit all the nodes of right subtree
            self.right.traverse_post_order()
        print(f"{self.val}-->", end=" ")    # Visit the root node


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print("TPO:", end=" ")
root.traverse_pre_order()
print("\nTIO", end=" ")
root.traverse_in_order()
print("\nTPO",end=" ")
root.traverse_post_order()


