''' Question:
*   Given a binary tree, determine if it is a valid binary search tree.
*   https://leetcode.com/problems/validate-binary-search-tree/
'''

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import math


def is_valid_BST(root: TreeNode) -> bool:
    def is_valid_node(node, min_, max_):
        if node is None:
            return True

        if not (min_ < node.val < max_):
            return False

        return is_valid_node(node.left, min_, node.val) and \
            is_valid_node(node.right, node.val, max_)

    return is_valid_node(root, -math.inf, math.inf)

# Time complexity: O(N)
# Space complexity: O(N)
