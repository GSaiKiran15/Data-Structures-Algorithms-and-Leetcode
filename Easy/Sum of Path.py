def pathSum(root, targetSum):
    def dfs(node, val):
        if not node:
            return False
        val += node.val
        if not node.left and not node.right:
            return val == targetSum
        return dfs(node.left) or dfs(node.right)
    return dfs(root, 0)