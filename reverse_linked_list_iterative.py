class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def reverseLinkedList(head):
    prev = None
    curr = head

    while curr:
        nextNode = curr.next
        curr.next = prev
        prev = curr
        curr = nextNode
    
    return prev