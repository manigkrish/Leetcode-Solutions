# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    # @param {TreeNode} root
    # @return {List[List[int]]}
    def levelOrder(self, root):
        if root is None:
            return []

        q = deque([root])  # Use deque for efficient queue operations
        levelOrderTraversal = []

        while q:
            level_size = len(q)
            level = []
            
            for _ in range(level_size):
                node = q.popleft()  # Dequeue from the front
                level.append(node.val)
                
                if node.left:
                    q.append(node.left)  # Enqueue left child
                if node.right:
                    q.append(node.right)  # Enqueue right child

            levelOrderTraversal.append(level)

        return levelOrderTraversal
