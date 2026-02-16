from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head
        while n > 0 and right:
            right = right.next
            n -= 1
        while right:
            right = right.next
            left = left.next
        left.next = left.next.next
        return dummy.next

        # l = 0
        # it = head
        # while it:
        #     l += 1
        #     it = it.next
        # dist = l - n
        # if dist == 0:
        #     return head.next
        # it = head
        # while it and dist-1 > 0:
        #     it = it.next
        #     dist -= 1
        # if it.next:
        #     it.next = it.next.next
        # else:
        #     it.next = None
        # return head


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
    # Input: head = [1,2,3,4,5], n = 2
    # Output: [1,2,3,5]
    print("Example 1:")
    head_1 = create_linked_list([1, 2, 3, 4, 5])
    print("Input:", print_linked_list(head_1))
    result_1 = solution.removeNthFromEnd(head_1, 2)
    print("Output:", print_linked_list(result_1))
    print("-" * 20)
    
    # Example 2
    # Input: head = [1], n = 1
    # Output: []
    print("Example 2:")
    head_2 = create_linked_list([1])
    print("Input:", print_linked_list(head_2))
    result_2 = solution.removeNthFromEnd(head_2, 1)
    print("Output:", print_linked_list(result_2))
    print("-" * 20)

    # Example 3
    # Input: head = [1,2], n = 1
    # Output: [1]
    print("Example 3:")
    head_3 = create_linked_list([1, 2])
    print("Input:", print_linked_list(head_3))
    result_3 = solution.removeNthFromEnd(head_3, 1)
    print("Output:", print_linked_list(result_3))
