''' Question:
*   Given a binary tree, return the level order traversal of the
*   nodes' values as an array
*   https://leetcode.com/problems/binary-tree-level-order-traversal/
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


def level_order_values(root: TreeNode) -> List[List[int]]:

    if root is None:
        return []

    values = []
    q = deque([root])

    while q:
        level_count = len(q)
        level_values = []
        for i in range(level_count):
            current = q.popleft()
            values.append(current.val)
            if current.left is not None:
                q.append(current.left)
            if current.right is not None:
                q.append(current.right)

        values.append(level_values)

    return values

# Time complexity: O(N)
# Space complexity: O(N)
