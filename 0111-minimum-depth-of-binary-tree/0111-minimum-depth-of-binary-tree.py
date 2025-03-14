# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = righ
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        
        left = self.minDepth(root.left) if root.left else sys.maxsize
        right = self.minDepth(root.right) if root.right else sys.maxsize

        return 1 + min(left, right)
