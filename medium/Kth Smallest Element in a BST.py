class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        values = []
        def inorder(root):
            if not root:
                return None
            if root.left:
                inorder(root.left)
            values.append(root.val)
            if root.right:
                inorder(root.right)
        inorder(root)
        return values[k-1]