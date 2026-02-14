from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev

# Helper functions for local testing
def create_linked_list(arr: List[int]) -> Optional[ListNode]:
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

def print_linked_list(head: Optional[ListNode]) -> List[int]:
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result

if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    # Input: head = [1,2,3,4,5]
    # Output: [5,4,3,2,1]
    head_1 = create_linked_list([1, 2, 3, 4, 5])
    print("Example 1 Input:", print_linked_list(head_1))
    reversed_head_1 = solution.reverseList(head_1)
    print("Example 1 Output:", print_linked_list(reversed_head_1))
    
    print("-" * 20)
    
    # Test Case 2
    # Input: head = [1,2]
    # Output: [2,1]
    head_2 = create_linked_list([1, 2])
    print("Example 2 Input:", print_linked_list(head_2))
    reversed_head_2 = solution.reverseList(head_2)
    print("Example 2 Output:", print_linked_list(reversed_head_2))

