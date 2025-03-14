# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if root is None:
            return []
        else:
            paths = []
            current = root
            s = []
            s.append(current)
            s.append(str(current.val))

            while s:
                path = s.pop()
                current = s.pop()

                if not current.left and not current.right:
                    paths.append(path)

                if current.right:
                    rightstr = path + "->" + str(current.right.val)
                    s.append(current.right)
                    s.append(rightstr)

                if current.left:
                    leftstr = path + "->" + str(current.left.val)
                    s.append(current.left)
                    s.append(leftstr)

            return paths
