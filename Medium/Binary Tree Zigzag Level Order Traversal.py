def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([root]) if root else deque()
        left_to_right = False
        res = []
        while queue:
            level = []
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                if left_to_right:
                    level.append(node.val)
                else:
                    level.insert(0, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level[::-1])
            left_to_right = not left_to_right
        return res