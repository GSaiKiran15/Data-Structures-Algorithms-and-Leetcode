from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val})"

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        

# Helper function to build a tree from a level-order traversal list
def build_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while i < len(values):
        current = queue.popleft()
        
        # Left child
        if i < len(values) and values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1
        
        # Right child
        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1
        
    return root

# Helper function to convert the flattened tree (linked list) to a list for verification
def tree_to_list(root):
    res = []
    curr = root
    while curr:
        res.append(curr.val)
        if curr.left: # Flattened tree should not have left children
            res.append("Error: Left child exists!")
            break
        curr = curr.right
    return res

if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    # Input: root = [1,2,5,3,4,null,6]
    # Expected Output: [1,null,2,null,3,null,4,null,5,null,6]
    # Note: The output list represents the right pointers.
    tree1 = build_tree([1, 2, 5, 3, 4, None, 6])
    solution.flatten(tree1)
    print(f"Test case 1 (Expected: [1, 2, 3, 4, 5, 6]): {tree_to_list(tree1)}")
    
    # Test Case 2
    # Input: root = []
    # Expected Output: []
    tree2 = build_tree([])
    solution.flatten(tree2)
    print(f"Test case 2 (Expected: []): {tree_to_list(tree2)}")

    # Test Case 3
    # Input: root = [0]
    # Expected Output: [0]
    tree3 = build_tree([0])
    solution.flatten(tree3)
    print(f"Test case 3 (Expected: [0]): {tree_to_list(tree3)}")
