# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return True
        elif head != None and head.next == None:
            return True
        else:
            fast = head
            slow = head
            stack = []
            
            # Traverse the list with fast and slow pointers
            while fast != None and fast.next != None:
                stack.append(slow.val)
                slow = slow.next
                fast = fast.next.next
            
            # If the list has odd number of elements, skip the middle element
            if fast != None:
                slow = slow.next
            
            # Compare the second half of the list with the stack
            while slow != None:
                if not stack or slow.val != stack.pop():
                    return False
                slow = slow.next
            
            return True