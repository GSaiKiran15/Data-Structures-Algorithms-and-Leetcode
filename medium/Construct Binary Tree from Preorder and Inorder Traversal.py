# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1: mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid + 1:])
        return root

if __name__ == "__main__":
    # Example Test Case
    # Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
    # Output: [3,9,20,null,null,15,7]
    
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    
    sol = Solution()
    root = sol.buildTree(preorder, inorder)
    
    def print_tree(node):
        if not node:
            return "[]"
        queue = [node]
        result = []
        while queue:
            curr = queue.pop(0)
            if curr:
                result.append(str(curr.val))
                queue.append(curr.left)
                queue.append(curr.right)
            else:
                result.append("null")
        
        # Clean up trailing 'null' values for cleaner output
        while result and result[-1] == "null":
            result.pop()
            
        return "[" + ",".join(result) + "]"

    print(f"Preorder: {preorder}")
    print(f"Inorder:  {inorder}")
    print(f"Resulting Tree (Level Order): {print_tree(root)}")
