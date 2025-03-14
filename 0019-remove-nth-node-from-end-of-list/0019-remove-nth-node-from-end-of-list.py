# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # If the list is empty, return None
        if head == None:
            return head
        
        # Create a dummy node to handle edge cases (e.g., removing the head)
        dummy = ListNode(0)
        dummy.next = head
        
        # Initialize two pointers, fast and slow, both starting at the dummy node
        fast = dummy
        slow = dummy
        
        # Move the fast pointer n steps ahead
        for i in range(n):
            fast = fast.next
        
        # Move both pointers until fast reaches the last node
        while fast.next != None:
            fast = fast.next
            slow = slow.next
        
        # Remove the nth node from the end by updating the next pointer of the slow node
        slow.next = slow.next.next
        
        # Return the head of the modified list
        return dummy.next