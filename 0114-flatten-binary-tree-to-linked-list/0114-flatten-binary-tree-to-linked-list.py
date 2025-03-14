# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root == None:
            return root
        stack = []
        current = root
        while (stack != [] or current != None):
            if current.right != None:
                stack.append(current.right)
            if current.left != None:
                current.right = current.left
                current.left = None
            else:
                if stack != []:
                    temp = stack.pop()
                    current.right = temp
            current = current.right