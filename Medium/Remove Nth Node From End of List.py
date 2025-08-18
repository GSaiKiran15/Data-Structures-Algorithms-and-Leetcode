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
def removeNthFromEnd(head, n):
    l = 0
    curr = head
    while curr:
        curr = curr.next
        l += 1
    pointer = 0
    curr = head
    while curr:
        if pointer == (l - n - 1):
            curr.next = curr.next.next
            break
        else:
            curr = curr.next
            pointer += 1
    return head
        
        

# ====== Test Here ======
if __name__ == "__main__":
    # Build linked list from Python list
    test_list = build_linked_list([1])
    
    print("Original list:")
    print_linked_list(test_list)

    # Run your function
    result = removeNthFromEnd(test_list, 1)

    print("After running function:")
    print_linked_list(result)
