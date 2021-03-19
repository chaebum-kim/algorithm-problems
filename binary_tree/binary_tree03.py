''' Question:
*   Given a binary tree, imagine you're standing to the right of the tree.
*   Return an array of the values of the nodes you can see ordred from
*   top to bottom.
'''

from binary_tree import BinaryTree


# Breadth first search approach
def get_visible_nodes(binary_tree: BinaryTree) -> list:

    if binary_tree.root is None:
        return []

    q = [binary_tree.root]
    result = []

    while q:
        length = len(q)
        count = 0

        while count < length:
            node = q.pop(0)
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
            count += 1

        result.append(node.key)

    return result

# Time complexity: O(n)
# Space complexity: O(n) -- depends on size(width) of tree


# Depth first search approach
def get_visible_nodes2(binary_tree: BinaryTree) -> list:
    values = []
    node_traverse(binary_tree.root, level=0, values=values)
    return values


def node_traverse(node: BinaryTree.BinaryTreeNode, level: int, values: list) -> list:

    if node is None:
        return None

    if len(values) == level:
        values.append(node.key)

    node_traverse(node.right, level+1, values)
    node_traverse(node.left, level+1, values)

# Time complexity: O(n)
# Space complexity: O(n) -- depends on height of tree


# Tests
if __name__ == '__main__':
    binary_tree1 = BinaryTree().make_tree_from_list(
        [10, 2, 11, 1, 8, 13, 9])
    binary_tree2 = BinaryTree().make_tree_from_list([1])
    binary_tree3 = BinaryTree()

    # Breadth first search
    print(get_visible_nodes(binary_tree1))
    print(get_visible_nodes(binary_tree2))
    print(get_visible_nodes(binary_tree3))

    # Depth first search
    print(get_visible_nodes2(binary_tree1))
    print(get_visible_nodes2(binary_tree2))
    print(get_visible_nodes2(binary_tree3))
