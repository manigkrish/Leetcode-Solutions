# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        else:
            stack = []
            paths = []
            current = root

            stack.append(current)
            stack.append([current.val])
            stack.append(current.val)

            while stack:
                pathsum = stack.pop()
                path = stack.pop()
                curr = stack.pop()

                if curr.left is None and curr.right is None:
                    if pathsum == sum:
                        paths.append(path)

                if curr.right:
                    right_path = path + [curr.right.val]
                    right_sum = pathsum + curr.right.val
                    stack.append(curr.right)
                    stack.append(right_path)
                    stack.append(right_sum)

                if curr.left:
                    left_path = path + [curr.left.val]
                    left_sum = pathsum + curr.left.val
                    stack.append(curr.left)
                    stack.append(left_path)
                    stack.append(left_sum)

            return paths