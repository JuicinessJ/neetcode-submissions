class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True

        adj_lst = { i: [] for i in range(n) }

        for key, value in edges:
            if key not in adj_lst:
                adj_lst[key] = []

            if value not in adj_lst:
                adj_lst[value] = []

            adj_lst[key].append(value)
            adj_lst[value].append(key)

        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False

            visited.add(node)

            for edge in adj_lst[node]:
                if edge == parent:
                    continue

                if not dfs(edge, node):
                    return False

            return True

        return dfs(0, -1) and len(visited) == n
        

"""
I am given a list of edges in the format as [a, b], where a and b, are the pairs connected, so for example [0, 1], [0, 2], 0 has two children, 1 and 2.

We've also been given an additional int, this helps track the number of edges exist, in order, from 0 to n - 1

I am asked to determine if the list I am given creates a tree, which is defined by levels, where nodes are connected to a level above or below, and not together on the same level, and not more than 1 level at a time.

As if nodes are connecting together on the same level, or levels more than 1 at a time, this creates a graph instead.

With the input I am given, I should start with creating an adjacency list (map), where the key is a of [a, b], and the values are b. 
This associate pairs that are found together when iterating through the list.
To create this list, we'll first start with looping through the input extracting the key and value, by using for key, value in edges: ...
or in other languages key = edges[i][0], values = edges[i][1]...

Then using the adjacency list, we'll map each key to their values appending into the list by: adj_lst = {} to start, then adj_lst[key].append(value).

But in python, we first need to check if the key is in the adj_lst first, if not we do: adj_lst[key] = [], then we can start appending, this replaces the use of importing...

After creating the adjacency list, we then need to check if the structure we are given is a tree or graph, a tree is where at each level, they only connect to nodes a level above or below, regardless of number of edges, meaning 1 node can have more than 1 parent, and 1 child.

A graph follows the same logic, but can connect to different levels, and can have cycles.

I believe to solve this problem, I need to check for cycles, in this case, I'll use a DFS approach, where I will maintain a visited set, this is just a set stored will nodes we are visiting, we start with calling the first value inside the adj_lst, using the provided int by looping from 0 to n - 1.

We check if the adj_lst[i] == [], as edge, if true, we return and check i + 1, if false, use recursion by looping through all adj_lst[i] edges.

If we determine a cycle, we stop, and return False, and if not we return True, this is caused by checking if appending a new node into our visited set already exist within the set.
"""