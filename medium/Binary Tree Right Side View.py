"""
Binary Tree Right Side View

Problem: Given a binary tree, return a list of the right side view of the tree.
The right side view consists of the last node at each level when viewed from the right.

Approach: Use level-order traversal (BFS) to process the tree level by level.
For each level, take the last (rightmost) node value.
"""

from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
            
        queue = [root]
        res = []
        while queue:
            res.append(queue[-1].val)
            for _ in range(len(queue)):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res


# Test cases
if __name__ == "__main__":
    # Example 1: [1,2,3,null,5,null,4]
    #       1
    #      / \
    #     2   3
    #      \   \
    #       5   4
    # Output: [1,3,4]
    
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.right = TreeNode(5)
    root1.right.right = TreeNode(4)
    
    sol = Solution()
    print("Example 1:", sol.rightSideView(root1))  # Expected: [1, 3, 4]
    
    # Example 2: [1,null,3]
    #       1
    #        \
    #         3
    # Output: [1,3]
    
    root2 = TreeNode(1)
    root2.right = TreeNode(3)
    
    print("Example 2:", sol.rightSideView(root2))  # Expected: [1, 3]
    
    # Example 3: []
    # Output: []
    
    print("Example 3:", sol.rightSideView(None))  # Expected: []
