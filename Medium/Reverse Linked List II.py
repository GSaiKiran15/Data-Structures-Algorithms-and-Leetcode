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
def reverseList(head, left, right):
    dummy = ListNode(0, head)
    leftPrev, cur = dummy, head
    for i in range(left - 1):
        leftPrev, cur = cur, cur.next
    prev = None
    for i in range(right - left + 1):
        tmpNext = cur.next
        cur.next = prev
        prev, cur = cur, tmpNext
    leftPrev.next.next = cur
    leftPrev.next = prev
    return dummy.next
        

# ====== Test Here ======
if __name__ == "__main__":
    # Build linked list from Python list
    test_list = build_linked_list([1, 2, 3, 4, 5])
    
    print("Original list:")
    print_linked_list(test_list)

    # Run your function
    result = reverseList(test_list, 2, 4)

    print("After running function:")
    print_linked_list(result)
