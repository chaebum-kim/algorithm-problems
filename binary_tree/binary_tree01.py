''' Question:
*   Given a binary tree, find its maximum depth. 
*   Maximum depth is the number of nodes along the longest path
*   from the root node to the furthest leaf node.
'''

from binary_tree import BinaryTree


def max_depth(node, depth):

    if node is None:
        return depth

    depth += 1
    return max([max_depth(node.left, depth), max_depth(node.right, depth)])

# Time complexity: O(n)
# Space complexity: O(n)


if __name__ == '__main__':
    binary_tree = BinaryTree().make_tree_from_list([3, 2, 5, 4, 10, 1])
    print(max_depth(binary_tree.root, 0))
