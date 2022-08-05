from data_structures.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    """
    Put docstring here
    """

    # def __init__(self):
    #     # initialization here
    #     pass

    def add(self, value):
        """
        wrap value in a Node and add it at correct spot
        """
        node = Node(value)
        if not self.root:
            self.root = node

        def track(root, add_node):
            if root is None:
                return

            if add_node.value < root.value:
                if root.left is None:
                    # spot available
                    root.left = add_node
                else:
                    track(root.left, add_node)
            else:
                if root.right is None:
                    # spot available
                    root.right = add_node
                else:
                    track(root.right, add_node)

        track(self.root, node)

    def contains(self, target):

        def track(root):
            if root is None:
                return False

            if target == root.value:
                return True

            if target < root.value:
                return track(root.left)
            else:
                return track(root.right)

        return track(self.root)

