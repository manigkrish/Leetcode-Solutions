# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getHeight(self, root):
        if root == None:
            return 0
        leftHeight = self.getHeight(root.left)
        if leftHeight == -1:
            return -1
        rightHeight = self.getHeight(root.right)
        if rightHeight == -1:
            return -1
        heightDiff = abs(leftHeight - rightHeight)
        if heightDiff > 1:
            return -1
        else:
            return max(leftHeight, rightHeight) + 1

    def isBalanced(self, root):
        if self.getHeight(root) == -1:
            return False
        else:
            return True