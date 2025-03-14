# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.__prev = None
        self.__node1 = None
        self.__node2 = None

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.recoverTreeHelp(root)
        temp = self.__node1.val
        self.__node1.val = self.__node2.val
        self.__node2.val = temp

    def recoverTreeHelp(self, root):
        if root is None:
            return

        self.recoverTreeHelp(root.left)

        if self.__prev is not None:
            if self.__prev.val > root.val:
                if self.__node1 is None:
                    self.__node1 = self.__prev
                self.__node2 = root

        self.__prev = root
        self.recoverTreeHelp(root.right)
        