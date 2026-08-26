class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # we need to do construct a topological ordering from a DAG
        # this is an ordering such that u -> v implies that u comes before v in the ordering
        # we create a TO by appending a thing to the stack only after processing its neighbours
        # then just reverse the stack
        
        adj = [[] for _ in range(numCourses)] # index i = nodes that i points into
        for dest, src in prerequisites:
            adj[src].append(dest)

        visited = [0] * numCourses
        stack = []

        def dfs(node, stack, visited):
            visited[node] = 1

            for neighbour in adj[node]:
                if visited[neighbour] == 1:
                    return False

                elif visited[neighbour] == 0:
                    if not dfs(neighbour, stack, visited):
                        return False

            stack.append(node)
            visited[node] = 2
            return True

        for i in range(numCourses):
            if not dfs(i, stack, visited):
                return []

        return stack[::-1]