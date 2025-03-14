# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # Base case: If the root is None, return None
        if root == None:
            return None
        
        # If the root is either p or q, return the root
        if root == p or root == q:
            return root
        
        # Recursively search for p and q in the left subtree
        left = self.lowestCommonAncestor(root.left, p, q)
        
        # Recursively search for p and q in the right subtree
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # If both left and right are not None, it means p and q are found in different subtrees,
        # so the current root is the LCA
        if left != None and right != None:
            return root
        
        # If left is None, return right (either p or q is found in the right subtree)
        if left == None:
            return right
        # Otherwise, return left (either p or q is found in the left subtree)
        else:
            return left