# ===== Linked List LeetCode Template =====

# Node definition (same as LeetCode)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __repr__(self):
        return f"{self.val}"

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
def reverseList(head, x):
    smaller = []
    greater = []
    cur = head
    while cur:
        if cur.val < x:
            smaller.append(cur.val)
        else:
            greater.append(cur.val)
        cur = cur.next
    dummy = ListNode(0)
    a = dummy
    cur = head
    smaller.extend(greater)
    for i in smaller:
        a.next = ListNode(i)
        a = a.next
    return dummy.next    
        
        

# ====== Test Here ======
if __name__ == "__main__":
    # Build linked list from Python list
    test_list = build_linked_list([1,4,3,2,5,2])
    
    print("Original list:")
    print_linked_list(test_list)
    x = 3
    # Run your function
    result = reverseList(test_list, x)

    print("After running function:")
    print_linked_list(result)
