def maxDepth(self, root) -> int:
    if root==None:
        return 0
    l=self.maxDepth(root.left)
    r=self.maxDepth(root.right)
    return 1+max(l,r)