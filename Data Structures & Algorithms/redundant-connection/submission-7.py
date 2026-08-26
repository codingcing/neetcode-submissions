class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
            # a tree has n-1 edges for some n vertices
            # since we have one too many, it means n = len(edges)
            n = len(edges)
            parents = {i: i for i in list(range(1, n+1))} # parents[i] = parent of node i, initialise each node to be its own parent

            def find_parent(node):
                if parents[node] != node:
                    # we do PATH COMPRESSION to compress paths between a node and its ROOT
                    # the ROOT will be the only element which is its own parent
                    parents[node] = find_parent(parents[node])
                return parents[node]

            num_components = n
            for node_a, node_b in edges:
                root_a = find_parent(node_a)
                root_b = find_parent(node_b)

                if root_a == root_b:
                    return [node_a, node_b]

                parents[root_a] = root_b

            return edges[-1]