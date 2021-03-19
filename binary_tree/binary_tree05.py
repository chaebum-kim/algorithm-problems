''' Question:
*   Given a binary tree, determine if it is a valid binary search tree.
'''

from binary_tree import BinaryTree
import math


def validate_binary_search_tree(binary_tree: BinaryTree) -> bool:
    return validate_nodes(binary_tree.root, -math.inf, math.inf)


def validate_nodes(node: BinaryTree.BinaryTreeNode, floor: int, ceiling: int):

    if not node:
        return True

    if node.key < floor or node.key > ceiling:
        return False

    return validate_nodes(node.left, floor=floor, ceiling=node.key)\
        and validate_nodes(node.right, floor=node.key, ceiling=ceiling)

# Time complexity: O(n)
# Space complexity: O(n)


# Test
if __name__ == '__main__':
    binary_tree1 = BinaryTree().make_tree_from_list(
        [15, 12, 17, 10, 19, 16, 18])
    binary_tree2 = BinaryTree().make_tree_from_list(
        [15, 12, 18, 10, 14, 13, 20])
    binary_tree3 = BinaryTree().make_tree_from_list([12, 7, 18, 5, 9, 16, 25])
    binary_tree4 = BinaryTree().make_tree_from_list([1])

    print(validate_binary_search_tree(binary_tree1))
    print(validate_binary_search_tree(binary_tree2))
    print(validate_binary_search_tree(binary_tree3))
    print(validate_binary_search_tree(binary_tree4))
