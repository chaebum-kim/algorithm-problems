
class BinaryTree:

    class BinaryTreeNode:

        def __init__(self, key):
            self.key = key
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, key: int):
        node = self.BinaryTreeNode(key)

        parent = None
        current = self.root
        while current is not None:
            parent = current
            if current.left is None:
                current = current.left
            else:
                current = current.right

        if parent is None:
            self.root = node
        elif parent.left is None:
            parent.left = node
        else:
            parent.right = node

    def make_tree_from_list(self, nums: list):
        if not nums:
            return self

        is_left = True
        self.root = self.BinaryTreeNode(nums.pop(0))
        q = [self.root]

        for num in nums:
            if num is None:
                current = None
            else:
                current = self.BinaryTreeNode(num)
                q.append(current)

            if is_left:
                parent = q.pop(0)
                parent.left = current
                is_left = False
            else:
                parent.right = current
                is_left = True

        return self

    def tree_print(self):
        q = [self.root]
        result = []
        while q:
            length = len(q)
            count = 0
            values = []

            while count < length:
                current = q.pop(0)
                if current is not None:
                    values.append(current.key)
                    q.append(current.left)
                    q.append(current.right)
                else:
                    values.append(None)
                count += 1

            if q:
                result.append(values)

        print(result)


if __name__ == '__main__':
    binary_tree = BinaryTree().make_tree_from_list(
        [1, 2, 3, 4, 5, None, 6, None, None, None, 7, None, None, 8])
    binary_tree.tree_print()

    binary_tree.insert(10)
    binary_tree.tree_print()
