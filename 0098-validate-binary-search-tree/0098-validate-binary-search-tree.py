# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.lastPrinted = -sys.maxsize - 1
    def isValidBST(self, root):
        if root == None:
            return True
        if self.isValidBST(root.left) == False:
            return False
        data = root.val
        if data <= self.lastPrinted:
            return False
        self.lastPrinted = data
        if self.isValidBST(root.right) == False:
            return False
        return True
