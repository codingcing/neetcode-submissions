class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # it feels like we need to do some combination of DFS and dijkstra's

        adj = [[] for _ in range(n)] # j in adj[i] = i points to j

        for frm, to, price in flights:
            adj[frm].append([price, to])

        # maintain some memory of where you have been
        # just plain dfs

        minCost = float('inf')

        def dfs(curr, visited, cost):
            nonlocal minCost
        
            if len(visited) > k+1 or cost > minCost:
                return
            
            if curr == dst:
                minCost = min(cost, minCost)
                return

            for price, to in adj[curr]:
                if to not in visited:
                    cop = visited.copy()
                    cop.add(to)
                    dfs(to, cop, cost + price)
            
            return

        for price, to in adj[src]:
            visited = set()
            visited.add(to)
            dfs(to, visited, price)
        
        return minCost if minCost != float('inf') else -1


