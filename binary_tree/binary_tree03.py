''' Question:
*   Given a binary tree, imagine you're standing to the right of the tree.
*   Return an array of the values of the nodes you can see ordred from
*   top to bottom.
*   https://leetcode.com/problems/binary-tree-right-side-view/
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from collections import deque


# Breadth first search approach
def right_side_view_bfs(root: TreeNode) -> List[int]:

    if root is None:
        return []

    values = []
    q = deque([root])
    while q:
        level_count = len(q)
        for i in range(level_count):
            current = q.popleft()
            if current.left is not None:
                q.append(current.left)
            if current.right is not None:
                q.append(current.right)
        values.append(current.val)

    return values

# Time complexity: O(N)
# Space complexity: O(N) -- depends on the size(width) of tree


# Depth first search approach
def right_side_view_dfs(root: TreeNode) -> List[int]:
    def dfs_traverse(node: TreeNode, values: list, level: int):
        if node is None:
            return None
        if len(values) == level:
            values.append(node.val)
        level += 1
        dfs_traverse(node.right, values, level)
        dfs_traverse(node.left, values, level)

    if root is None:
        return []

    values = []
    dfs_traverse(root, values, 0)
    return values

# Time complexity: O(N)
# Space complexity: O(N) -- depends on height of tree
