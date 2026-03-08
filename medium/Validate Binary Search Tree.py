from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, high, low):
            if not node:
                return True
            if not (node.val < high and node.val > low):
                return False
            
            return (validate(node.left, node.val, low) and validate(node.right, high, node.val))
            
        return validate(root, float("inf"), float("-inf"))

if __name__ == "__main__":
    # Test cases to verify the implementation
    def build_tree(nodes):
        if not nodes:
            return None
        root = TreeNode(nodes[0])
        queue = [root]
        i = 1
        while i < len(nodes):
            curr = queue.pop(0)
            if nodes[i] is not None:
                curr.left = TreeNode(nodes[i])
                queue.append(curr.left)
            i += 1
            if i < len(nodes) and nodes[i] is not None:
                curr.right = TreeNode(nodes[i])
                queue.append(curr.right)
            i += 1
        return root

    sol = Solution()
    
    # Example 1: root = [2,1,3], Output: true
    root1 = build_tree([2, 1, 3])
    print(f"Test case 1: {sol.isValidBST(root1)}")

    # Example 2: root = [5,1,4,None,None,3,6], Output: false
    root2 = build_tree([5,4,6, None, None,3,7])
    print(f"Test case 2: {sol.isValidBST(root2)}")
