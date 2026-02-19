from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __repr__(self):
        return f"ListNode({self.val})"

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        pointer = dummy
        small_tail = dummy  # tracks end of the < x section
        cur = head
        while cur:
            if cur.val >= x:
                pointer.next = ListNode(cur.val, None)
                pointer = pointer.next
            else:
                # Insert after small_tail, keeping the >= x chain connected
                new_node = ListNode(cur.val, small_tail.next)
                small_tail.next = new_node
                small_tail = new_node
                # If pointer hasn't moved past dummy, update it so it doesn't overwrite
                if pointer == dummy:
                    pointer = small_tail
            cur = cur.next
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
    # Input: head = [1,4,3,2,5,2], x = 3
    # Output: [1,2,2,4,3,5]
    print("Example 1:")
    head_1 = create_linked_list([1, 4, 3, 2, 5, 2])
    print("Input:", print_linked_list(head_1), "x = 3")
    result_1 = solution.partition(head_1, 3)
    print("Output:", print_linked_list(result_1))
    print("-" * 20)
    
    # Example 2
    # Input: head = [2,1], x = 2
    # Output: [1,2]
    print("Example 2:")
    head_2 = create_linked_list([2, 1])
    print("Input:", print_linked_list(head_2), "x = 2")
    result_2 = solution.partition(head_2, 2)
    print("Output:", print_linked_list(result_2))
