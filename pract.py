class BinarySearchTree:
# This is Binary Search Tree Program
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self,data):
        if data == self.data:
            return None
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)
        if data > self.data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)

    def inorder_traversal(self):
        elements = []
        if self.data is None:
            print("Tree is empty!")
            return
        if self.left:
            elements += self.left.inorder_traversal()
        elements.append(self.data)
        if self.right:
            elements += self.right.inorder_traversal()
        return elements

    def search(self,data):
        if data == self.data:
            return print(f"Yes the data:{data} you are searching for exist in the tree!")
        if data < self.data:
            if self.left:
                return self.left.search(data)
            else:
                return None

        if data > self.data:
            if self.right:
                return self.right.search(data)
            else:
                return None

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def delete(self,data):
        if data < self.data:
            if self.left:
                self.left = self.left.delete(data)
        elif data > self.data:
            if self.right:
                self.right = self.right.delete(data)

        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.right
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)
        return self

def build_tree(elements):
    root = BinarySearchTree(elements[0])
    for i in range(len(elements)):
        root.add_child(elements[i])
    return  root

if __name__ == '__main__':
    number = [17, 4, 1, 20, 9, 23, 18, 34]
    tree = build_tree(number)
    print(tree.inorder_traversal())
    print(tree.search(17))
    print(tree.delete(18))
    print(tree.inorder_traversal())