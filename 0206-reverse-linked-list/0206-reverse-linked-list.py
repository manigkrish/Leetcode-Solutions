# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        prev = None
        current = head

        while current:
            next_node = current.next  # Save next node
            current.next = prev       # Reverse current node's pointer
            prev = current            # Move prev forward
            current = next_node       # Move current forward

        return prev