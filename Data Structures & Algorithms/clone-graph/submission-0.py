"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

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


"""
I am given a node that is connected to the rest of a graph, 
and asked to return a deep copy of the same graph.

This means every node within the graph is copied, however, the old graph's nodes,
are not reused, instead cloned.
Meaning new nodes and new graph...

This also means when we are cloning the nodes, 
we need to replicate the cloning node with their value and neighbor(s).

However, an issue we may run into is when we are cloning the old graph,
the nodes we want to connect to may not exist during the process.

Which means, I will need to either use a dummy node, 
which will update or discover a different method.

If we use a dummy node, how would we return back to this dummy node to update?
We could use a hashmap where the key is the old node address,
and the value will be the new node.
"""