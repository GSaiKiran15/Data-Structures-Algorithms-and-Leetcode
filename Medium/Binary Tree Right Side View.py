from collections import deque

class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))

def bfs(r):
    queue = deque([r]) if r else deque()
    res = []
    while queue:
        size = len(queue)
        res.append(queue[-1].val)
        for _ in range(size):    
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return(res)
        
bfs(root)
