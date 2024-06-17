# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Establish two pointers
        prev = curr = head
        
        # While two pointers are not null
        while curr:
            # Re-assign 'next' of each node to a node with a different value
            while curr and prev.val == curr.val:
                curr = curr.next
            prev.next = curr
            
            # Move both pointers to the node with a different value
            prev = curr
        
        # Return the head node
        return head

#Time: O(n)linear Space: O(1)linear
