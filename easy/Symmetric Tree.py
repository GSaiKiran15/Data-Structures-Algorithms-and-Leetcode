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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        def dfs(leftChild, rightChild):
            if not leftChild and not rightChild:
                return True
            if not leftChild or not rightChild:
                return False
            return (leftChild.val == rightChild.val and dfs(leftChild.left, rightChild.right) and dfs(leftChild.right, rightChild.left))
        return dfs(root.left, root.right)

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
    
    # Test Case 1: Symmetric Tree
    # Input: root = [1,2,2,3,4,4,3]
    # Expected Output: True
    tree1 = build_tree([1, 2, 2, 3, 4, 4, 3])
    print(f"Test case 1 (Expected: True): {solution.isSymmetric(tree1)}")
    
    # Test Case 2: Asymmetric Tree
    # Input: root = [1,2,2,null,3,null,3]
    # Expected Output: False
    tree2 = build_tree([1, 2, 2, None, 3, None, 3])
    print(f"Test case 2 (Expected: False): {solution.isSymmetric(tree2)}")

    # Test Case 3: Empty Tree
    # Input: root = []
    # Expected Output: True
    tree3 = build_tree([])
    print(f"Test case 3 (Expected: True): {solution.isSymmetric(tree3)}")
