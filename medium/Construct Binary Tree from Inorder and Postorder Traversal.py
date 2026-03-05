# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:
        """
        Constructs a binary tree from inorder and postorder traversal.
        
        Args:
            inorder: A list of integers representing the inorder traversal.
            postorder: A list of integers representing the postorder traversal.
            
        Returns:
            The root node of the constructed binary tree.
        """
        # TODO: Implement the solution
        pass

if __name__ == "__main__":
    # Example Test Case
    # Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
    # Output: [3,9,20,null,null,15,7]
    
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]
    
    sol = Solution()
    root = sol.buildTree(inorder, postorder)
    
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

    print(f"Inorder:   {inorder}")
    print(f"Postorder: {postorder}")
    print(f"Resulting Tree (Level Order): {print_tree(root)}")
