from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def __repr__(self):
        return f"TreeNode({self.val})"

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

# Helper function to build tree from level-order traversal list
def build_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while i < len(values):
        current = queue.pop(0)
        
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

if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    # Input: root = [1,2,3,4,5,6]
    # Expected Output: 6
    tree1 = build_tree([1, 2, 3, 4, 5, 6])
    print(f"Test case 1 (Expected: 6): {solution.countNodes(tree1)}")
    
    # Test Case 2
    # Input: root = []
    # Expected Output: 0
    tree2 = build_tree([])
    print(f"Test case 2 (Expected: 0): {solution.countNodes(tree2)}")

    # Test Case 3
    # Input: root = [1]
    # Expected Output: 1
    tree3 = build_tree([1])
    print(f"Test case 3 (Expected: 1): {solution.countNodes(tree3)}")
