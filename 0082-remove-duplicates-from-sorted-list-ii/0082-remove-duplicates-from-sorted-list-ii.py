# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        
        # Dictionary to count occurrences of each value
        dup_dict = {}
        current = head
        
        # First pass: count occurrences of each value
        while current:
            if current.val in dup_dict:
                dup_dict[current.val] += 1
            else:
                dup_dict[current.val] = 1
            current = current.next
        
        # Second pass: collect unique values
        unique_values = []
        current = head
        while current:
            if dup_dict[current.val] == 1:
                unique_values.append(current.val)
            current = current.next
        
        # If no unique values, return None
        if not unique_values:
            return None
        
        # Create a new linked list from unique values
        new_head = ListNode(unique_values[0])
        current_new = new_head
        for value in unique_values[1:]:
            current_new.next = ListNode(value)
            current_new = current_new.next
        
        return new_head