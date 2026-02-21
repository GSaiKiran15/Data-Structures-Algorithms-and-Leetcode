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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        

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
        if values[i] is not None:
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
    
    # Test Case 1: Identical Trees
    # Input: p = [1,2,3], q = [1,2,3]
    # Output: True
    tree1_p = build_tree([1, 2, 3])
    tree1_q = build_tree([1, 2, 3])
    print(f"Test case 1 (Expected: True): {solution.isSameTree(tree1_p, tree1_q)}")
    
    # Test Case 2: Different Structure
    # Input: p = [1,2], q = [1,null,2]
    # Output: False
    tree2_p = build_tree([1, 2])
    tree2_q = build_tree([1, None, 2])
    print(f"Test case 2 (Expected: False): {solution.isSameTree(tree2_p, tree2_q)}")

    # Test Case 3: Different Values
    # Input: p = [1,2,1], q = [1,1,2]
    # Output: False
    tree3_p = build_tree([1, 2, 1])
    tree3_q = build_tree([1, 1, 2])
    print(f"Test case 3 (Expected: False): {solution.isSameTree(tree3_p, tree3_q)}")
