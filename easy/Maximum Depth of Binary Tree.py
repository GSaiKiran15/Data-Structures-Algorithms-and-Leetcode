from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val})"

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.right), self.maxDepth(root.left))

# Helper function for local testing
def create_binary_tree(arr: List[Optional[int]]) -> Optional[TreeNode]:
    if not arr:
        return None
    
    nodes = [TreeNode(val) if val is not None else None for val in arr]
    root = nodes[0]
    queue = [root]
    i = 1
    
    while queue and i < len(nodes):
        curr = queue.pop(0)
        if curr:
            if i < len(nodes) and nodes[i]:
                curr.left = nodes[i]
                queue.append(curr.left)
            i += 1
            if i < len(nodes) and nodes[i]:
                curr.right = nodes[i]
                queue.append(curr.right)
            i += 1
            
    return root

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    # Input: root = [3,9,20,null,null,15,7]
    # Output: 3
    print("Example 1:")
    root_1 = create_binary_tree([3, 9, 20, None, None, 15, 7])
    print("Input Tree Root:", root_1)
    result_1 = solution.maxDepth(root_1)
    print("Output:", result_1)
    print("-" * 20)
    
    # Example 2
    # Input: root = [1,null,2]
    # Output: 2
    print("Example 2:")
    root_2 = create_binary_tree([1, None, 2])
    print("Input Tree Root:", root_2)
    result_2 = solution.maxDepth(root_2)
    print("Output:", result_2)
