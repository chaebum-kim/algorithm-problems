''' Question:
*   Given a binary tree, find its maximum depth. 
*   Maximum depth is the number of nodes along the longest path
*   from the root node to the furthest leaf node.
*   https://leetcode.com/problems/maximum-depth-of-binary-tree/
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root: TreeNode) -> int:
    def measure_depth(node: TreeNode, depth: int) -> int:
        if node is None:
            return depth
        depth += 1
        return max(measure_depth(node.left, depth), measure_depth(node.right, depth))

    return measure_depth(root, 1)


# Time complexity: O(N)
# Space complexity: O(N)
