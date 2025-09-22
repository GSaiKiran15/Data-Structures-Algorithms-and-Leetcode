from collections import deque

class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))

def levelOrder(root):
    queue = deque([root]) if root else deque()
    res = [] 
    while queue:
        level = []
        size = len(queue)
        for _ in range(size):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
                level.append(node.left.val)
            if node.right:
                queue.append(node.right)
                level.append(node.right.val)
        if level:
            res.append(level)
    print(res)
    return res

levelOrder(root)