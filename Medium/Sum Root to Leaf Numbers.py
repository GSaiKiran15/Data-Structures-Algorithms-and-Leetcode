def dfs(node, curr):
    if not node:
        return 0
    curr = (curr * 10) + node.val
    if not node.left or not node.right:
        return curr
    return dfs(node.left, curr) + dfs(node.right, curr)    