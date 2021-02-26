
class BinaryTree:

    class BinaryTreeNode:

        def __init__(self, key):
            self.key = key
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def append(self, key: int):
        node = self.BinaryTreeNode(key)

        parent = None
        current = self.root
        while current is not None:
            parent = current
            if current.key < node.key:
                current = current.right
            else:
                current = current.left

        if parent is None:
            self.root = node
        elif parent.key < node.key:
            parent.right = node
        else:
            parent.left = node

    def make_tree_from_list(self, nums: list):
        for num in nums:
            self.append(num)
        return self
