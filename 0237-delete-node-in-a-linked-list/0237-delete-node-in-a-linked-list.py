# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node is None or node.next is None:
            # Edge cases: either no node is provided or it's the last node,
            # which can't be handled by this method.
            return

        # Copy the next node's value into the current node.
        next_node = node.next
        node.val = next_node.val
        node.next = next_node.next