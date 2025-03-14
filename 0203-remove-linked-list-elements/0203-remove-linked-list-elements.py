# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # Create a dummy node that points to the head of the list
        dummy = ListNode(0)
        dummy.next = head
        
        # Use prev to keep track of the previous node
        prev = dummy
        
        # Traverse the list
        while head:
            if head.val == val:
                # Skip the current node by updating prev.next
                prev.next = head.next
            else:
                # Move prev to the current node
                prev = head
            # Move head to the next node
            head = head.next
        
        # Return the new head of the list
        return dummy.next