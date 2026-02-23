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
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, num):
            if not node:
                return 0
            num = num * 10 + node.val
            if not node.left and not node.right:
                return num
            return dfs(node.left, num) + dfs(node.right, num)
        return dfs(root, 0)
            

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
    # Input: root = [1,2,3]
    # Expected Output: 25
    # Explanation:
    # The root-to-leaf path 1->2 represents the number 12.
    # The root-to-leaf path 1->3 represents the number 13.
    # Therefore, sum = 12 + 13 = 25.
    tree1 = build_tree([1, 2, 3])
    print(f"Test case 1 (Expected: 25): {solution.sumNumbers(tree1)}")
    
    # Test Case 2
    # Input: root = [4,9,0,5,1]
    # Expected Output: 1026
    # Explanation:
    # The root-to-leaf path 4->9->5 represents the number 495.
    # The root-to-leaf path 4->9->1 represents the number 491.
    # The root-to-leaf path 4->0 represents the number 40.
    # Therefore, sum = 495 + 491 + 40 = 1026.
    tree2 = build_tree([4, 9, 0, 5, 1])
    print(f"Test case 2 (Expected: 1026): {solution.sumNumbers(tree2)}")
