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