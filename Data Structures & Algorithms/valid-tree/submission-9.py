class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # a graph is a tree iff it is connected and has no cycles
        # it also needs to have n-1 edges if it has n vertices (implied by above)
        # we use a process called DSU to assign each vertex a 'parent' even in an 
        # undirected graph

        parents = list(range(n)) # parents[i] = parent of node i, initialise each node to be its own parent

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
                # a and b have the same root, joining them will create a cycle
                # that means following some edges created a CYCLE -> invalid tree
                return False

            # make one ROOT the parent of another
            parents[root_a] = root_b

            num_components -= 1

        # also possible to have no cycles, BUT more than one connected component

        return num_components == 1