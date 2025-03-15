# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import Queue

class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def levelOrderBottom(self, root):
        if root is None:
            return []
        else:
            q = Queue.Queue()  # Use Queue.Queue() in Python 2
            q.put(root)
            q.put("#")

            levelOrderTraversal = []
            level = []
            stack = []

            while not q.empty():
                node = q.get()

                if node == "#":
                    if not q.empty():
                        q.put("#")
                    stack.append(level)
                    level = []
                else:
                    level.append(node.val)
                    if node.left:
                        q.put(node.left)
                    if node.right:
                        q.put(node.right)

            while stack:
                levelOrderTraversal.append(stack.pop())

            return levelOrderTraversal