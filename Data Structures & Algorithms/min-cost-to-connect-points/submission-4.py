import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # intuition: it shouldnt matter which point you start from
        # we just use dijsktra's - 1, adjacency graph, 2, greedy heap based dfs
        n = len(points)
        if n==1: return 0

        adj = [[] for _ in range(n)] # adj[i] = nodes that i points to
        for i in range(n):
            for j in range(i+1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                d = abs(x1-x2) + abs(y1-y2)
                adj[i].append([d,j]) 
                adj[j].append([d,i])

        visited = [False] * n
        minHeap = [[0, 0]] # cost, idx to add
        cost = 0
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if visited[n1]:
                continue

            visited[n1] = True
            cost += w1

            for w2, n2 in adj[n1]:
                if not visited[n2]:
                    heapq.heappush(minHeap, [w2, n2])

        return cost