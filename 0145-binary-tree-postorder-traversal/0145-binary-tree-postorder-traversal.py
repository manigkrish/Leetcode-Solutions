# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        
        stack = []
        out_stack = []
        stack.append(root)
        
        while stack:
            current = stack.pop()
            out_stack.append(current.val)
            
            # Push left child first so that right is processed first
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)
        
        # Reverse the output to get postorder traversal
        return out_stack[::-1]