from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        rabbit, tortoise = head, head
        while rabbit and tortoise:
            if rabbit and rabbit.next.next:
                rabbit = rabbit.next.next
                tortoise = tortoise.next
            else:
                return False
            if rabbit == tortoise:
                return True
        return False

# Helper to create a linked list with a cycle
def create_linked_list_with_cycle(values, pos):
    if not values:
        return None
    
    nodes = []
    for val in values:
        nodes.append(ListNode(val))
    
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    
    if pos != -1 and 0 <= pos < len(nodes):
        nodes[-1].next = nodes[pos]
        
    return nodes[0]

if __name__ == "__main__":
    # Test Case 1: list = [3,2,0,-4], pos = 1 (cycle exists)
    values = [3, 2, 0, -4]
    pos = 1
    head = create_linked_list_with_cycle(values, pos)
    
    solution = Solution()
    print(f"Test Case 1 Has Cycle: {solution.hasCycle(head)}") # Expected: True

    # Test Case 2: list = [1,2], pos = 0 (cycle exists)
    values = [1, 2]
    pos = 0
    head = create_linked_list_with_cycle(values, pos)
    print(f"Test Case 2 Has Cycle: {solution.hasCycle(head)}") # Expected: True

    # Test Case 3: list = [1], pos = -1 (no cycle)
    values = [1]
    pos = -1
    head = create_linked_list_with_cycle(values, pos)
    print(f"Test Case 3 Has Cycle: {solution.hasCycle(head)}") # Expected: False
