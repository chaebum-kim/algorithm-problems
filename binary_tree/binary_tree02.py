''' Question:
*   Given a binary tree, return the level order traversal of the
*   nodes' values as an array
'''

from binary_tree import BinaryTree


def level_order_values(binary_tree: BinaryTree) -> list:

    if binary_tree.root is None:
        return []

    result = []
    q = [binary_tree.root]

    while q:
        length = len(q)
        count = 0
        values = []

        while count < length:
            node = q.pop(0)
            values.append(node.key)
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
            count += 1

        result.append(values)

    return result

# Time complexity: O(n)
# Space complexity: O(n)


# Test
if __name__ == '__main__':
    binary_tree = BinaryTree().make_tree_from_list([4, 2, 8, 1, 5, 9, 3])
    print(level_order_values(binary_tree))

    binary_tree = BinaryTree()
    print(level_order_values(binary_tree))

    binary_tree = BinaryTree()
    binary_tree.append(3)
    print(level_order_values(binary_tree))
