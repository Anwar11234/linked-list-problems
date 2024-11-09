# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(head):
        """
        Do not return anything, modify head in-place instead.
        """
        # first phase: find the middle of the linked list
        slow = head
        fast = head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second_half = slow.next
        slow.next = None # split the 2 halves
        
        # second phase: reverse the right half
        prev = None
        while second_half:
            next_node = second_half.next
            second_half.next = prev
            prev = second_half
            second_half = next_node
        
        # third phase: merge the 2 halves alternatively
        first_half = head
        second_half = prev
        
        while first_half and second_half:
            next1 = first_half.next
            next2 = second_half.next
            
            first_half.next = second_half
            second_half.next = next1
            
            first_half = next1
            second_half = next2