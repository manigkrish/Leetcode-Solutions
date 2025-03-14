# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys

class Solution(object):
    def __init__(self):
        self.maxSum = -sys.maxsize - 1

    def maxPathSum(self, root):
        self.findMax(root)
        return self.maxSum

    def findMax(self, root):
        if root is None:
            return 0
        left = max(0, self.findMax(root.left))  # Only consider positive contributions
        right = max(0, self.findMax(root.right))  # Only consider positive contributions
        self.maxSum = max(self.maxSum, root.val + left + right)
        return root.val + max(left, right)