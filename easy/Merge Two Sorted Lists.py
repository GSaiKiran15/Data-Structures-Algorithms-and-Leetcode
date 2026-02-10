from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy_head = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                dummy_head.next = list1
                list1 = list1.next
            else:
                dummy_head.next = list2
                list2 = list2.next
            dummy_head = dummy_head.next
        if list1:
            dummy_head.next = list1
        elif list2:
            dummy_head.next = list2
        return dummy.next

# Helper to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper to print linked list
def print_linked_list(head):
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    print(values)

if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: list1 = [1,2,4], list2 = [1,3,4]
    l1 = create_linked_list([1, 2, 4])
    l2 = create_linked_list([1, 3, 4])
    merged = solution.mergeTwoLists(l1, l2)
    print("Test Case 1 Output:", end=" ")
    print_linked_list(merged) # Expected: [1, 1, 2, 3, 4, 4]

    # Test Case 2: list1 = [], list2 = []
    l1 = create_linked_list([])
    l2 = create_linked_list([])
    merged = solution.mergeTwoLists(l1, l2)
    print("Test Case 2 Output:", end=" ")
    print_linked_list(merged) # Expected: []

    # Test Case 3: list1 = [], list2 = [0]
    l1 = create_linked_list([])
    l2 = create_linked_list([0])
    merged = solution.mergeTwoLists(l1, l2)
    print("Test Case 3 Output:", end=" ")
    print_linked_list(merged) # Expected: [0]
