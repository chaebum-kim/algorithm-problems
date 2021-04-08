''' Question:
*   Given a complete binary tree, count the number of nodes.
*   https://leetcode.com/problems/count-complete-tree-nodes/
'''

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import math


def count_nodes1(root: TreeNode) -> int:
    def node_exists(root, height, index_to_find) -> bool:
        left, right = 0, 2**height-1
        current = root
        for i in range(height):
            middle = math.ceil((left+right)/2)
            if index_to_find >= middle:
                current = current.right
                left = middle
            else:
                current = current.left
                right = middle - 1
        return current is not None

    if root is None:
        return 0

    height = 0
    current = root.left
    while current is not None:
        height += 1
        current = current.left
    upper = 2**height-1

    left, right = 0, upper
    while left < right:
        middle = math.ceil((left+right)/2)
        if node_exists(root, height, middle):
            left = middle
        else:
            right = middle - 1

    return upper + left + 1


def count_nodes2(root: TreeNode) -> int:

    if root is None:
        return 0

    height = 0
    current = root.left
    while current is not None:
        height += 1
        current = current.left
    upper = 2**height-1

    # Count the number of last nodes
    left, right = 0, upper
    while left < right:
        middle = math.ceil((left + right) / 2)
        dirs = format(middle, f'0{height}b')
        current = root

        for direction in dirs:
            if direction == '0':
                current = current.left
            else:
                current = current.right

        if current is not None:
            left = middle
        else:
            right = middle - 1

    return upper + left + 1

# Time complexity: O(h^2) -- h = height of tree
# Space complexity: O(1)


# Test
binary_tree1 = BinaryTree().make_tree_from_list([x for x in range(1, 16)])
binary_tree2 = BinaryTree().make_tree_from_list([x for x in range(1, 9)])
binary_tree3 = BinaryTree().make_tree_from_list([x for x in range(1, 25)])

print(count_nodes(binary_tree1))
print(count_nodes(binary_tree2))
print(count_nodes(binary_tree3))
