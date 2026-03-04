from typing import Optional, List
from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def __repr__(self):
        return f"Node({self.val})"

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        curr = root
        while curr:
            # Dummy node to track the head of the next level
            dummy = Node(0)
            tail = dummy
            
            # Traverse the current level using 'next' pointers
            while curr:
                if curr.left:
                    tail.next = curr.left
                    tail = tail.next
                if curr.right:
                    tail.next = curr.right
                    tail = tail.next
                curr = curr.next
            
            # Move to the start of the next level
            curr = dummy.next
            
        return root
            
                 

# Helper function to build a tree from a level-order traversal list
def build_tree(values):
    if not values:
        return None
    root = Node(values[0])
    queue = deque([root])
    i = 1
    while i < len(values):
        current = queue.popleft()
        
        # Left child
        if i < len(values) and values[i] is not None:
            current.left = Node(values[i])
            queue.append(current.left)
        i += 1
        
        # Right child
        if i < len(values) and values[i] is not None:
            current.right = Node(values[i])
            queue.append(current.right)
        i += 1
        
    return root

# Helper function to verify next pointers by level
def get_next_pointers_by_level(root):
    if not root:
        return []
    
    res = []
    level_start = root
    while level_start:
        curr = level_start
        level_values = []
        next_level_start = None
        
        while curr:
            level_values.append(curr.val)
            # Find the first node of the next level
            if not next_level_start:
                if curr.left:
                    next_level_start = curr.left
                elif curr.right:
                    next_level_start = curr.right
            curr = curr.next
            
        res.append(level_values)
        
        # If we didn't find next_level_start from the current level's children, 
        # we need to search further down or end. 
        # For a standard level-order traversal verification:
        if not next_level_start:
            # Search for the start of the next level in the current level's siblings
            # This is tricky for non-perfect trees. A simpler way is BFS for verification:
            break 
            
        level_start = next_level_start
        
    return res

# Alternative simpler verification using BFS to collect levels and check 'next' continuity
def verify_next_pointers(root):
    if not root:
        return []
    
    output = []
    curr_level_start = root
    while curr_level_start:
        curr = curr_level_start
        level_vals = []
        while curr:
            level_vals.append(curr.val)
            curr = curr.next
        output.append(level_vals)
        
        # Move to the first available child in the current level to start the next level
        temp = curr_level_start
        curr_level_start = None
        while temp:
            if temp.left:
                curr_level_start = temp.left
                break
            if temp.right:
                curr_level_start = temp.right
                break
            temp = temp.next
            
    return output

if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    # Input: root = [1,2,3,4,5,null,7]
    # Expected Output: [1,#,2,3,#,4,5,7,#]
    tree1 = build_tree([1, 2, 3, 4, 5, None, 7])
    solution.connect(tree1)
    print(f"Test case 1 (Levels via next pointers): {verify_next_pointers(tree1)}")
    
    # Test Case 2
    # Input: root = []
    # Expected Output: []
    tree2 = build_tree([])
    solution.connect(tree2)
    print(f"Test case 2: {verify_next_pointers(tree2)}")
