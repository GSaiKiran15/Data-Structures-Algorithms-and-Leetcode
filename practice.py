from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def __repr__(self):
        return f"ListNode({self.val})"

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        rabbit, tortoise = head, head
        while rabbit and tortoise:
            if rabbit.next and rabbit.next.next:
                rabbit = rabbit.next.next
                tortoise = tortoise.next
            else:
                return False
            if rabbit == tortoise:
                return True
        return False

# Helper function to create a linked list with a cycle
def create_linked_list_with_cycle(values, pos):
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    nodes = [head]
    
    for i in range(1, len(values)):
        new_node = ListNode(values[i])
        current.next = new_node
        current = new_node
        nodes.append(new_node)
    
    # Create the cycle
    if pos != -1:
        current.next = nodes[pos]
        
    return head

if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1: Cycle exists
    # Input: head = [3,2,0,-4], pos = 1
    # Expected Output: True
    list1 = create_linked_list_with_cycle([3, 2, 0, -4], 1)
    print(f"Test case 1 (Expected: True): {solution.hasCycle(list1)}")
    
    # Test Case 2: Cycle exists at head
    # Input: head = [1,2], pos = 0
    # Expected Output: True
    list2 = create_linked_list_with_cycle([1, 2], 0)
    print(f"Test case 2 (Expected: True): {solution.hasCycle(list2)}")

    # Test Case 3: No cycle
    # Input: head = [1], pos = -1
    # Expected Output: False
    list3 = create_linked_list_with_cycle([1], -1)
    print(f"Test case 3 (Expected: False): {solution.hasCycle(list3)}")
