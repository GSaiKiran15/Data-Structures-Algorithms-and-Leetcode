# ---------- Node class definition ----------
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    # Add this for easy debugging and readable prints
    def __repr__(self):
        return f"Node({self.val})"


# ---------- Helper: Build graph from adjacency list ----------
# Input format: adjacency list like [[2,4],[1,3],[2,4],[1,3]]
# (same as LeetCode’s cloneGraph input)
def build_graph(adj_list):
    if not adj_list:
        return None
    nodes = [Node(i + 1) for i in range(len(adj_list))]
    for idx, neighbors in enumerate(adj_list):
        nodes[idx].neighbors = [nodes[n - 1] for n in neighbors]
    return nodes[0]  # return reference to starting node


# ---------- Helper: Print graph in readable form ----------
def print_graph(node):
    from collections import deque
    visited = set()
    q = deque([node])
    print("\nGraph adjacency view:")
    while q:
        n = q.popleft()
        if n in visited:
            continue
        visited.add(n)
        print(f"Node {n.val} -> {[nei.val for nei in n.neighbors]}")
        for nei in n.neighbors:
            if nei not in visited:
                q.append(nei)


# ---------- Your solution ----------
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        oldToNew = {}
        
        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            
            copy = Node(node.val)
            oldToNew[node] = copy
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy
        
        return dfs(node)


# ---------- Debug / Test Section ----------
if __name__ == "__main__":
    # Example graph (same as LeetCode example)
    # 1 -- 2
    # |    |
    # 4 -- 3
    adj_list = [[2, 4], [1, 3], [2, 4], [1, 3]]

    original = build_graph(adj_list)
    print("Original Graph:")
    print_graph(original)

    sol = Solution()
    cloned = sol.cloneGraph(original)

    print("\nCloned Graph:")
    print_graph(cloned)