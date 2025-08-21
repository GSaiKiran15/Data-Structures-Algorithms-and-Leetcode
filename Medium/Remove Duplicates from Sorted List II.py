# ===== Linked List LeetCode Template =====

# Node definition (same as LeetCode)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __repr__(self):
        return f"{self.val}"
    
    def debug_repr(self):
        nxt = self.next.val if self.next else None
        nxt2 = self.next.next.val if self.next and self.next.next else None
        return f"curr={self.val}, next={nxt}, next.next={nxt2}"

# Helper: build linked list from Python list
def build_linked_list(values):
    if not values:  # empty list case
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper: print linked list as a Python list
def print_linked_list(head):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    print(arr)

# ====== Example Function (Replace with your LeetCode solution) ======
def reverseList(head):
    dummy = ListNode(0, head)
    start = dummy
    curr = head
    while curr and curr.next:
        if curr.val == curr.next.val:
            curr = curr.next
            while curr.val == start.next.val:
                curr = curr.next
                if not curr:
                    break
            start.next = curr
        else:
            start = start.next
            curr = curr.next
    return dummy.next
        
        

# ====== Test Here ======
if __name__ == "__main__":
    # Build linked list from Python list
    test_list = build_linked_list([1,1])
    
    print("Original list:")
    print_linked_list(test_list)

    # Run your function
    result = reverseList(test_list)

    print("After running function:")
    print_linked_list(result)
