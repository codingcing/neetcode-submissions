class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # need to look for cycles in directed graph
        adj = [[] for _ in range(numCourses)] # index i holds nodes that i points to
        for dest, src in prerequisites:
            adj[src].append(dest)

        visited = [0] * numCourses # 0 not visited, 1 visiting, 2 visited

        def dfs(node, visited):
            visited[node] = 1

            for neighbour in adj[node]:
                if visited[neighbour] == 1:
                    return False

                elif visited[neighbour] == 0:
                    if not dfs(neighbour, visited):
                        return False

            visited[node] = 2
            return True

        for i in range(numCourses):
            if not dfs(i, visited):
                return False

        return True