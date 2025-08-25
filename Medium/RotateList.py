# ===== Linked List LeetCode Template =====

# Node definition (same as LeetCode)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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
def reverseList(head, k):
    if head is None:
        return None
    if head.next is None:
        return head
    n = 1
    old_head = head
    while old_head.next:
        old_head = old_head.next
        n += 1
    old_head.next = head
    new_tail = head
    for _ in range(n - k % n - 1):
        new_tail = new_tail.next
    new_head = new_tail.next
    new_tail.next = None
    return new_head
        

# ====== Test Here ======
if __name__ == "__main__":
    # Build linked list from Python list
    test_list = build_linked_list([0, 1, 2])
    
    print("Original list:")
    print_linked_list(test_list)

    # Run your function
    result = reverseList(test_list, 4)

    print("After running function:")
    print_linked_list(result)
