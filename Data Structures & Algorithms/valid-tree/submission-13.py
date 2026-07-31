class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True

        adj_lst = { i: [] for i in range(n) }

        for key, value in edges:
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