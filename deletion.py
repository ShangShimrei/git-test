class BinarySearchTree:
    """
    class for Binary_search
    """

    def __init__(self, data):
        """
        Constructor for parameters
        Args:
            data:
        """
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            """
            if data to be inserted already exists, return
            """
            return
        if data < self.data:
            """
            check if the data is less than the root node
            if it is less than root node, then add to the left side of subtree
            """
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)
        else:
            """
            if the data is greater than the root node, add in the right side of subtree
            """
            if self.right:  # check if the left node exists some elements
                self.right.add_child(data)
            else:  # if no elements exists, or if left node is empty,
                # create a new node on left subtree, thereby calling from the class - root node
                self.right = BinarySearchTree(data)

    def in_order_traversal(self):
        elements = []
        if self.left:  # Visit the left node
            elements += self.left.in_order_traversal()
        elements.append(self.data)  # Visit the root node
        if self.right:  # Visit the right node
            elements += self.right.in_order_traversal()
        return elements

    def search(self, val):
        if self.data == val:
            return True
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def find_max(self):
        if self.right is None:  # iterate through the right subtree until it reaches the leaf node
            return self.data    # return the data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:   # iterate through the left subtree until it reaches the leaf node
            return self.data    # return the data
        return self.left.find_min()

    def delete(self, value):

        if value < self.data:   # if the value is less than self.data
            if self.left:   # check for elements in left subtree
                self.left = self.left.delete(value)
                """
                recursively called delete method and update the left subtree
                """
        elif value > self.data:  # if the value is greater than self.data
            if self.right:  # check for elements in right subtree
                self.right = self.right.delete(value)
                """
                recursively called delete method and update the right subtree
                """
        else:
            if self.left is None and self.right is None:
                """
                if you reach the leaf node of both the subtree, return None
                """
                return None
            if self.left is None:   # if the left subtree has no left node than return the right node
                return self.right
            if self.right is None:  # if the right subtree has no right node than return right node
                return self.right
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)
        return self


def build_tree(elements):
    root = BinarySearchTree(elements[0])  # build the root node

    for i in range(1, len(elements)):  # Iterate through the set through the loop
        root.add_child(elements[i])
    return root


if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    numbers_tree = build_tree(numbers)

    print(numbers_tree.in_order_traversal())
    print(numbers_tree.search(21))
    print(numbers_tree.delete(1))
    print(numbers_tree.in_order_traversal())
