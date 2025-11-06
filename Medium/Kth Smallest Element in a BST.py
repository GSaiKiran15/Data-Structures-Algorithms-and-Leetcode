def kthSmallest(self, root, k) -> int:
    n = 0
    stack = []
    cur = root

    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        n += 1
        if n == k:
            return cur.val
        cur = cur.right

    # arr = []
    # def dfs(arr, root):
    #     if root is None:
    #         return 
    #     if len(arr) == k:
    #         return arr[-1]
    #     dfs(arr, root.left)
    #     arr.append(root.val)
    #     dfs(arr, root.right)
    # dfs(arr, root)
    # return arr[k-1]