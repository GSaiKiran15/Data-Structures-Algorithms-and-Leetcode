class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
    
def addTwoNumbers(head):
    carry = 0
    dummy = ListNode()
    curr = dummy
    l1 = head
    l2 = head
    while l1 or l2 or carry:
        total = l1.val + l2.val + carry
        carry, digit = divmod(total, 10)
        curr.next = ListNode(digit)
        curr = curr.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    return dummy.next