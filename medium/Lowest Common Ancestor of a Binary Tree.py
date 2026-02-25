from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
    def __repr__(self):
        return f"TreeNode({self.val})"

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root == p or root == q:
            return root
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        if l and r:
            return root
        else:
            return l or r
                


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

# Helper function to find a node with a specific value in the tree
def find_node(root, val):
    if not root:
        return None
    if root.val == val:
        return root
    left = find_node(root.left, val)
    if left:
        return left
    return find_node(root.right, val)

if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    # Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
    # Expected Output: 3
    tree1 = build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    p1 = find_node(tree1, 5)
    q1 = find_node(tree1, 1)
    result1 = solution.lowestCommonAncestor(tree1, p1, q1)
    print(f"Test case 1 (Expected: 3): {result1.val if result1 else 'None'}")
    
    # Test Case 2
    # Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
    # Expected Output: 5
    tree2 = build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    p2 = find_node(tree2, 5)
    q2 = find_node(tree2, 4)
    result2 = solution.lowestCommonAncestor(tree2, p2, q2)
    print(f"Test case 2 (Expected: 5): {result2.val if result2 else 'None'}")

    # Test Case 3
    # Input: root = [1,2], p = 1, q = 2
    # Expected Output: 1
    tree3 = build_tree([1, 2])
    p3 = find_node(tree3, 1)
    q3 = find_node(tree3, 2)
    result3 = solution.lowestCommonAncestor(tree3, p3, q3)
    print(f"Test case 3 (Expected: 1): {result3.val if result3 else 'None'}")
