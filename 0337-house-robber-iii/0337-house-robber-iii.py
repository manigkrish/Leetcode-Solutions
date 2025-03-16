# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        else:
            result = self.rob_max(root)
            return max(result[0], result[1])

    def rob_max(self, root):
        if root is None:
            return [0, 0]
        else:
            left_res = self.rob_max(root.left)
            right_res = self.rob_max(root.right)
            result = [0] * 2

            # Case 1: Rob this house (include current node's value)
            result[0] = root.val + left_res[1] + right_res[1]

            # Case 2: Don't rob this house (take max from children)
            result[1] = max(left_res[0], left_res[1]) + max(right_res[0], right_res[1])

            return result
