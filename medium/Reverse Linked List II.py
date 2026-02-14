from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        prev = None
        cur = head
        for _ in range(left-1):
            prev = cur
            cur = cur.next
        ans, successor = self.reverseList(cur, right - left, prev)
        if successor:
            ans.next = successor
        return head if left > 0 else ans

    def reverseList(self, head: Optional[ListNode], end, prev) -> Optional[ListNode]:
        print(head.val, end, prev.val)
        for _ in range(end):
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev, head
        

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
    # Input: head = [1,2,3,4,5], left = 2, right = 4
    # Output: [1,4,3,2,5]
    print("Test Case 1:")
    head_1 = create_linked_list([1, 2, 3, 4, 5])
    print("Input:", print_linked_list(head_1))
    reversed_head_1 = solution.reverseBetween(head_1, 2, 4)
    print("Output:", print_linked_list(reversed_head_1))
    
    print("-" * 20)
    
    # Test Case 2
    # Input: head = [5], left = 1, right = 1
    # Output: [5]
    print("Test Case 2:")
    head_2 = create_linked_list([5])
    print("Input:", print_linked_list(head_2))
    reversed_head_2 = solution.reverseBetween(head_2, 1, 1)
    print("Output:", print_linked_list(reversed_head_2))
