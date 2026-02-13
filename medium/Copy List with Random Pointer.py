from typing import Optional, List

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curToNewMap = {None : None}
        iterator = head
        while iterator:
            curToNewMap[iterator] = Node(iterator.val)
            iterator = iterator.next
        iterator = head
        while iterator:
            copy = curToNewMap[iterator]
            copy.next = curToNewMap[iterator.next]
            copy.random = curToNewMap[iterator.random]
            iterator = iterator.next
        return curToNewMap[head]

# Helper functions for local testing
def create_linked_list(data: List[List[Optional[int]]]) -> Optional[Node]:
    """
    Creates a linked list with random pointers based on the input list of [val, random_index].
    """
    if not data:
        return None
    
    # Step 1: Create all nodes
    nodes = [Node(val) for val, _ in data]
    
    # Step 2: Set next and random pointers
    for i, (_, random_index) in enumerate(data):
        if i < len(nodes) - 1:
            nodes[i].next = nodes[i+1]
        
        if random_index is not None:
            nodes[i].random = nodes[random_index]
            
    return nodes[0]

def print_linked_list(head: Optional[Node]) -> List[List[Optional[int]]]:
    """
    Converts the linked list back to the [[val, random_index], ...] format for verification.
    """
    if not head:
        return []
    
    # First pass: Map nodes to their indices to determine random_index
    node_to_index = {}
    curr = head
    index = 0
    while curr:
        node_to_index[curr] = index
        curr = curr.next
        index += 1
        
    # Second pass: Build the result list
    result = []
    curr = head
    while curr:
        random_index = node_to_index[curr.random] if curr.random else None
        result.append([curr.val, random_index])
        curr = curr.next
        
    return result

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    # Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
    head_data_1 = [[7,None],[13,0],[11,4],[10,2],[1,0]]
    head_1 = create_linked_list(head_data_1)
    print("Example 1 Input:", print_linked_list(head_1))
    copied_head_1 = solution.copyRandomList(head_1)
    print("Example 1 Output:", print_linked_list(copied_head_1))
    print("-" * 30)

    # Example 2
    # Input: head = [[1,1],[2,1]]
    head_data_2 = [[1,1],[2,1]]
    head_2 = create_linked_list(head_data_2)
    print("Example 2 Input:", print_linked_list(head_2))
    copied_head_2 = solution.copyRandomList(head_2)
    print("Example 2 Output:", print_linked_list(copied_head_2))
    print("-" * 30)

    # Example 3
    # Input: head = [[3,null],[3,0],[3,null]]
    head_data_3 = [[3,None],[3,0],[3,None]]
    head_3 = create_linked_list(head_data_3)
    print("Example 3 Input:", print_linked_list(head_3))
    copied_head_3 = solution.copyRandomList(head_3)
    print("Example 3 Output:", print_linked_list(copied_head_3))
