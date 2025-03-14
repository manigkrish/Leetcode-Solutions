# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    # Constructor to initialize the iterator
    def __init__(self, root):
        """
        Initializes the BSTIterator with the root of the BST.
        :param root: The root node of the binary search tree.
        """
        self.stack = []  # Stack to store nodes for in-order traversal
        self._push_left_subtree(root)  # Push the leftmost path to the stack

    def _push_left_subtree(self, node):
        """
        Helper function to push the leftmost path of the subtree rooted at `node` onto the stack.
        :param node: The root of the subtree.
        """
        while node:
            self.stack.append(node)
            node = node.left

    def hasNext(self):
        """
        Checks if there are more nodes to traverse.
        :return: True if there are more nodes, False otherwise.
        """
        return len(self.stack) > 0

    def next(self):
        """
        Returns the next smallest node's value in the BST.
        :return: The value of the next smallest node.
        """
        if not self.hasNext():
            raise Exception("No more elements in the BST.")

        next_node = self.stack.pop()  # Pop the next smallest node
        self._push_left_subtree(next_node.right)  # Push the leftmost path of the right subtree
        return next_node.val
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()