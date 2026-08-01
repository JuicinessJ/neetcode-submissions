class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not n:
            return 0

        adj_lst = { i: [] for i in range(n) }

        for key, value in edges:
            adj_lst[key].append(value)
            adj_lst[value].append(key)

        visited = set()

        def dfs(node):
            if node in visited:
                return

            visited.add(node)

            for neighbor in adj_lst[node]:
                if neighbor in visited:
                    continue 

                dfs(neighbor)

        total_comp = 0

        for i in range(n):
            if i not in visited:
                total_comp += 1
                dfs(i)
    
        return total_comp

"""
I am given a list of edges, and a integer, representing the expected number of nodes within the list, from 0 to n - 1.
Where this list could include individual nodes that are not connected to another, but will not be found within the provided list, such as edges = [[0,1],[1,2]], n = 5. 
Where we have nodes: [0,1,2,3,4], but 3 and 4 do not appear in the provided list, as they're not connected meaning individual nodes.

I am asked to return the number of connected components formed by the provided list, where each componenets can vary in lengths, from 2 or more nodes.
Where each componenets form a path, from node, to node, head to tail.
Cycles are not a concern, as they also are considered a componenet.
Individual nodes are also considered connected componenets, even though, they are not connected to any other nodes.

I should first start with creating an adjacency list, where we map each unique node to their connected nodes, since this is undirected, we should include a and b of [a, b] in each others list.
We also need to make sure we have keys for nodes that may not appear within the edges list.

This provides us a tool to support with traversing this graph, and allow for a DFS approach/recursive.

After we have created the adjacency list, we'll need to recurse through each node, for example if we have: n = 5, edges = [[0,1],[1,2],[3,4]].

Our 0, 1, 2 nodes are connected, we'll need to start with checking 0, see if this key has any values, if it does, we check its neighbors.
We'll check 1, we'll see 1 has 0 inside, but this previous node doesn't matter, and shouldn't impact anything, so we'll continue pass this.
It'll then need to check its other neighbors, 2.
While checking 2, we see its previous 1, ignore and continue and see no other connection.

We'll update our total of connected componenets.
This updated componenet needs to increment for every individual set of componenets.

This set will record the number of visited nodes we have seen, but this set needs to reset itself, after we've ended traversing that pair, before entering a new pair.
"""