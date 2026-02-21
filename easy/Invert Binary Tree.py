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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

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

# Helper function to convert tree to list for easy comparison/printing
def tree_to_list(root):
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        current = queue.pop(0)
        if current:
            result.append(current.val)
            queue.append(current.left)
            queue.append(current.right)
        else:
            result.append(None)
    
    # Remove trailing Nones to match LeetCode format
    while result and result[-1] is None:
        result.pop()
    return result

if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    # Input: root = [4,2,7,1,3,6,9]
    # Expected Output: [4,7,2,9,6,3,1]
    tree1 = build_tree([4, 2, 7, 1, 3, 6, 9])
    res1 = solution.invertTree(tree1)
    print(f"Test case 1 (Expected: [4, 7, 2, 9, 6, 3, 1]): {tree_to_list(res1)}")
    
    # Test Case 2
    # Input: root = [2,1,3]
    # Expected Output: [2,3,1]
    tree2 = build_tree([2, 1, 3])
    res2 = solution.invertTree(tree2)
    print(f"Test case 2 (Expected: [2, 3, 1]): {tree_to_list(res2)}")

    # Test Case 3
    # Input: root = []
    # Expected Output: []
    tree3 = build_tree([])
    res3 = solution.invertTree(tree3)
    print(f"Test case 3 (Expected: []): {tree_to_list(res3)}")
