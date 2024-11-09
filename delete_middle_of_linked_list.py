# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteMiddle(head):
    if head.next is None:
        return None
    
    prev = ListNode()
    prev.next = head
    slow = prev 
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    slow.next = slow.next.next
    
    return head