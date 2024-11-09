class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseBetween(head, left, right):
    dummy = ListNode(0, head)
    
    pre_left = dummy
    curr = head
    
    # move curr from head to left. head is at index1, and this loop executes left - 1 times
    # which is the distance between head and left.
    # so curr starts at index 1. get incremented left - 1 times, ends at left.
    for i in range(left - 1): 
        pre_left = curr
        curr = curr.next
    
    # curr is at left, pre_left is at left - 1. Start reversing nodes between left and right
    # right - left + 1 is the number of nodes from left to right.
    
    prev = None
    for i in range(right - left + 1):
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    
    # curr is at right + 1, prev is at right.
    # we need left.next to be right + 1 and we need pre_left.next to be right.
    
    pre_left.next.next = curr # pre_left.next = left
    pre_left.next = prev
    
    return dummy.next