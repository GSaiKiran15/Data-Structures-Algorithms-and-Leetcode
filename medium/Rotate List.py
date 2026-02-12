from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode(val={self.val}, next={self.next})"

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        
        l, tail = 1, head
        while tail.next:
            l += 1
            tail = tail.next
        k = k % l
        if k == 0:
            return head
        curHead = head
        for i in range(l - k - 1):
            curHead = curHead.next
        newHead = curHead.next
        curHead.next = None
        tail.next = head
        return newHead

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

    # Test Case 1: head = [1,2,3,4,5], k = 2 -> Expected Output: [4,5,1,2,3]
    head = create_linked_list([1, 2])
    k = 1
    print(f"Test Case 1 (k={k}): Original: ", end="")
    print_linked_list(create_linked_list([1, 2, 3, 4, 5]))
    result = solution.rotateRight(head, k)
    print("Output: ", end="")
    print_linked_list(result)
    print("-" * 20)

    # Test Case 2: head = [0,1,2], k = 4 -> Expected Output: [2,0,1]
    head = create_linked_list([0, 1, 2])
    k = 4
    print(f"Test Case 2 (k={k}): Original: ", end="")
    print_linked_list(create_linked_list([0, 1, 2]))
    result = solution.rotateRight(head, k)
    print("Output: ", end="")
    print_linked_list(result)
    print("-" * 20)
    
    # Test Case 3: head = [], k = 0 -> Expected Output: []
    # head = create_linked_list([])
    # k = 0
    # print(f"Test Case 3 (k={k}): Original: ", end="")
    # print_linked_list(create_linked_list([]))
    # result = solution.rotateRight(head, k)
    # print("Output: ", end="")
    # print_linked_list(result)
    # print("-" * 20)
