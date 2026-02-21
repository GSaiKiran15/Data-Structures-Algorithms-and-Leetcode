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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, cur_sum):
            if not node:
                return False
            cur_sum += node.val
            if not node.left and not node.right:
                return cur_sum == targetSum
            return (dfs(node.left, cur_sum) or dfs(node.right, cur_sum))
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
    # Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
    # Expected Output: True (Path: 5 -> 4 -> 11 -> 2)
    tree1 = build_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])
    print(f"Test case 1 (Expected: True): {solution.hasPathSum(tree1, 22)}")
    
    # Test Case 2
    # Input: root = [1,2,3], targetSum = 5
    # Expected Output: False
    tree2 = build_tree([1, 2, 3])
    print(f"Test case 2 (Expected: False): {solution.hasPathSum(tree2, 5)}")

    # Test Case 3
    # Input: root = [], targetSum = 0
    # Expected Output: False
    tree3 = build_tree([])
    print(f"Test case 3 (Expected: False): {solution.hasPathSum(tree3, 0)}")
