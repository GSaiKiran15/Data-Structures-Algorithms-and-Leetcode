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
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        res = []
        queue = deque([root])
        while queue:
            level_sum = 0
            level_len = len(queue)
            for i in range(level_len):
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level_sum / level_len)
        return res

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

if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    # Input: root = [3,9,20,null,null,15,7]
    # Expected Output: [3.00000, 14.50000, 11.00000]
    tree1 = build_tree([3, 9, 20, None, None, 15, 7])
    result1 = solution.averageOfLevels(tree1)
    print(f"Test case 1 (Expected: [3.0, 14.5, 11.0]): {result1}")
    
    # Test Case 2
    # Input: root = [3,9,20,15,7]
    # Expected Output: [3.00000, 14.50000, 11.00000]
    tree2 = build_tree([3, 9, 20, 15, 7])
    result2 = solution.averageOfLevels(tree2)
    print(f"Test case 2 (Expected: [3.0, 14.5, 11.0]): {result2}")
