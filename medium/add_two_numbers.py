from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode(val={self.val}, next={self.next})"

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        dummy = res
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            
            carry = total // 10
            digit = total % 10
            
            dummy.next = ListNode(digit)
            dummy = dummy.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return res.next

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

    # Test Case 1: l1 = [2,4,3], l2 = [5,6,4] -> Expected Output: [7,0,8]
    # Representing 342 + 465 = 807
    l1 = create_linked_list([2, 4, 3])
    l2 = create_linked_list([5, 6, 4])
    result = solution.addTwoNumbers(l1, l2)
    print("Test Case 1 Output:", end=" ")
    print_linked_list(result) 

    # Test Case 2: l1 = [0], l2 = [0] -> Expected Output: [0]
    l1 = create_linked_list([0])
    l2 = create_linked_list([0])
    result = solution.addTwoNumbers(l1, l2)
    print("Test Case 2 Output:", end=" ")
    print_linked_list(result)

    # Test Case 3: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9] -> Expected Output: [8,9,9,9,0,0,0,1]
    l1 = create_linked_list([9, 9, 9, 9, 9, 9, 9])
    l2 = create_linked_list([9, 9, 9, 9])
    result = solution.addTwoNumbers(l1, l2)
    print("Test Case 3 Output:", end=" ")
    print_linked_list(result)
