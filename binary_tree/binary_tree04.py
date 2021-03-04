''' Question:
*   Given a complete binary tree, count the number of nodes.
'''
from binary_tree import BinaryTree
import math


def count_nodes(binary_tree: BinaryTree) -> int:

    # Evaluate height of tree
    current = binary_tree.root
    height = 0
    while current is not None:
        height += 1
        current = current.left

    # Count the number of nodes except last nodes
    counter = 2 ** (height-1) - 1

    # Count the number of last nodes
    root = binary_tree.root
    left = 0
    right = counter

    while left < right:
        middle = math.ceil((left + right) / 2)
        dirs = format(middle, f'0{height-1}b')
        node = root

        for direction in dirs:
            if direction == '0':
                node = node.left
            else:
                node = node.right

        if node is not None:
            left = middle
        else:
            right = middle - 1

    counter += (left + 1)

    return counter

# Time complexity: O(h^2) -- h = height of tree
# Space complexity: O(1)


# Test
binary_tree1 = BinaryTree().make_tree_from_list([x for x in range(1, 16)])
binary_tree2 = BinaryTree().make_tree_from_list([x for x in range(1, 9)])
binary_tree3 = BinaryTree().make_tree_from_list([x for x in range(1, 25)])

print(count_nodes(binary_tree1))
print(count_nodes(binary_tree2))
print(count_nodes(binary_tree3))
