def countNodes(self, root):
    if not root: return 0

    def depth(node):
        d = 0
        while node:
            d += 1
            node = node.left
        return d

    left, right = depth(root.left), depth(root.right)
    if left == right:
        return (1 << left) + self.countNodes(root.right)
    else:
        return (1 << right) + self.countNodes(root.left)