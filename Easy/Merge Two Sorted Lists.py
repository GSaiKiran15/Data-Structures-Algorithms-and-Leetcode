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
def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    dummy = ListNode()
    curr = dummy
    while list1 and list2:
        if list1.val > list2.val:
            curr.next = list2
            list2 = list2.next
        else:
            curr.next = list1
            list1 = list1.next
        curr = curr.next
        
    if list1:
        curr.next = list1
        
    if list2:
        curr.next = list2
        
    return dummy.next

# ====== Test Here ======
if __name__ == "__main__":
    # Build linked list from Python list
    list1 = build_linked_list([-9, 3])
    list2 = build_linked_list([5, 7])


    # Run your function
    result = mergeTwoLists(list1, list2)

    print("After running function:")
    print_linked_list(result)
