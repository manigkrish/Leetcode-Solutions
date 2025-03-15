# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if root is None:
            return None
        else:
            stack = []
            node = root
            count = 0

            while stack or node:
                if node:
                    stack.append(node)
                    node = node.left
                else:
                    inorder_node = stack.pop()
                    count += 1
                    if count == k:
                        return inorder_node.val
                    node = inorder_node.right

            return None  # If k is out of range