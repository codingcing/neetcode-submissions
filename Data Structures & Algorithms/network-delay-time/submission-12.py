import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for i in range(n+1)] # idx: [[neighbours, weight]] where idx -> neighbour

        for src, dest, weight in times:
            adj[src].append([dest, weight])

        visited = {} # map node: shortest path from k to node
        minHeap = [[0, k]]
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue
            visited[n1] = w1

            for n2, w2 in adj[n1]:
                if n2 not in visited:
                    heapq.heappush(minHeap, [w1+w2, n2])
        
        return max(visited.values()) if len(visited) == n else -1