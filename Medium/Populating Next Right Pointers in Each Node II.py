from collections import deque

class Solution:
    def connect(self, root):
        if not root:
            return None
        root.next = None
        queue = deque([root])
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            for i in range(len(queue)):
                if i == len(queue)-1:
                    queue[i].next = None
                else:
                    queue[i].next = queue[i+1]
        return root