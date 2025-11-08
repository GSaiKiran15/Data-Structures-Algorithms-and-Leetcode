def isValidBST(root):
    def dfs(node, low='-inf', high='inf'):
        if not node:
            return True
        if not low < node.val < high:
            return False
        return dfs(node.left) and dfs(node.right)
    return dfs(root)