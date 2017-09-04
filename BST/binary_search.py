""" Node is defined as """
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    """ Insert method places a value onto an existing tree starting on the root """
    def insert(self, value):
        # If value bigger than node data then go right
        if value > self.data:
            # If empty then place on right subtree node
            if self.right is None:
                self.right = Node(value)
                return self
            # If not empty then call a recursion on right subtree node
            else:
                self.right.insert(value)
        # Similar if less than Node
        elif value < self.data:
            if self.left is None:
                self.left = Node(value)
                return self
            else:
                self.left.insert(value)
        # Throw a ValueError if we have an equality as this is not allowed
        else:
            return ValueError("No repeats allowed")

    """ Contains method checks if a value is inside a BST """
    def contains(self, value):
        print("Fired")
        if self.data == value:
            print("condition true")
            return True
        elif value > self.data:
            if self.right is None:
                return False
            else:
                self.right.contains(value)
        else:
            if self.left is None:
                return False
            else:
                self.left.contains(value)


def checkBST(root):
    pass


if __name__ == "__main__":
    my_tree = Node(4)
    my_tree.insert(5)
    my_tree.insert(12)
    my_tree.insert(8)
    print(my_tree.contains(5))



