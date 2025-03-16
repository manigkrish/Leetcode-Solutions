# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import Queue 

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def rightSideView(self, root):
        if root is None:
            return []
        else:
            q = Queue.Queue() 
            q.put(root)
            q.put("#")

            rightSideView = []
            level = []

            while not q.empty():
                node = q.get()

                if node == "#":
                    if not q.empty():
                        q.put("#")
                    if level:
                        rightSideView.append(level[-1])  
                    level = []
                else:
                    level.append(node.val)
                    if node.left:
                        q.put(node.left)
                    if node.right:
                        q.put(node.right)

            return rightSideView
