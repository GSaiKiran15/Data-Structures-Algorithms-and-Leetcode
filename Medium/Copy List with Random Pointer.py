# ===== Node definition for LeetCode 138 =====
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


# ===== Solution class (implement here) =====
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        oldToCopy = {None : None}
        cur = head
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next
        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next
        return oldToCopy[head]


# ===== Helpers for building & printing =====
def build_random_list(values, random_indices):
    """
    values: list of node values
    random_indices: list of indices for random pointers (-1 means None)
    """
    if not values:
        return None

    nodes = [Node(val) for val in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    for i, rand_idx in enumerate(random_indices):
        if rand_idx != -1:
            nodes[i].random = nodes[rand_idx]
    return nodes[0]


def print_random_list(head):
    """Prints list as [(val, random_val), ...]"""
    res = []
    curr = head
    while curr:
        res.append((curr.val, curr.random.val if curr.random else None))
        curr = curr.next
    print(res)


# ====== Test Here ======
if __name__ == "__main__":
    # Example: values = [7, 13, 11, 10, 1]
    # Random pointers:  [-1, 0, 4, 2, 0] (LeetCode example)
    head = build_random_list([7, 13, 11, 10, 1], [-1, 0, 4, 2, 0])

    print("Original list:")
    print_random_list(head)

    sol = Solution()
    copied = sol.copyRandomList(head)

    print("Copied list:")
    print_random_list(copied)
