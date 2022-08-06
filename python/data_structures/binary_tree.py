class BinaryTree:
    """
    Put docstring here
    """

    def __init__(self):
        # initialization here
        self.root = None

    def pre_order(self):

        values = []

        def track(root):

            if root is None:
                return

            # do the root (whatever job you're doing)
            values.append(root.value)

            # left
            track(root.left)

            # right
            track(root.right)

        track(self.root)

        return values


    def in_order(self):
        """
        left - root -right
        """

        values = []

        def track(root):
            if root is None:
                return

            # left
            track(root.left)
            # root
            values.append(root.value)
            # right
            track(root.right)

        track(self.root)

        return values

    def post_order(self):
        values = []

        def track(root):
            if root is None:
                return

            # left
            track(root.left)

            # right
            track(root.right)

            # root
            values.append(root.value)

        track(self.root)

        return values


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
