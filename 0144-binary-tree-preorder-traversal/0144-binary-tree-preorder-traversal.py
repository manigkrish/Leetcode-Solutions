# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root):
        if root == None:  # Base case: if the tree is empty, return an empty list
            return []
        else:
            preorderList = []  # List to store the result
            stack = []         # Stack to help with iterative traversal
            stack.append(root) # Start with the root node

            while stack != []:  # Continue until the stack is empty
                node = stack.pop()  # Pop the top node from the stack
                preorderList.append(node.val)  # Add its value to the result list

                # Push the right child first (so that the left child is processed first)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)

            return preorderList  # Return the result list