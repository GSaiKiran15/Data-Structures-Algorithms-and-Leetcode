from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __repr__(self):
        return f"ListNode({self.val})"

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        while head:
            while head.next and head.val == head.next.val:
                head = head.next
            if prev.next == head:
                prev = prev.next
            else:
                prev.next = head.next
            head = head.next
        return dummy.next 


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
    
    # Example 1
    # Input: head = [1,2,3,3,4,4,5]
    # Output: [1,2,5]
    print("Example 1:")
    head_1 = create_linked_list([1, 2, 3, 3, 4, 4, 5])
    print("Input:", print_linked_list(head_1))
    result_1 = solution.deleteDuplicates(head_1)
    print("Output:", print_linked_list(result_1))
    print("-" * 20)
    
    # Example 2
    # Input: head = [1,1,1,2,3]
    # Output: [2,3]
    print("Example 2:")
    head_2 = create_linked_list([1, 1, 1, 2, 3])
    print("Input:", print_linked_list(head_2))
    result_2 = solution.deleteDuplicates(head_2)
    print("Output:", print_linked_list(result_2))
