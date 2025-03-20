class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        # find parent
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # connect x and y
        y = self.find(y)
        x = self.find(x)

        if x != y:
            # short's parent will be long, and update the size
            if self.size[x] < self.size[y]:
                self.parent[x] = y
                self.size[y] += self.size[x]
            else:
                self.parent[y] = x
                self.size[x] += self.size[y]


class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        # 1. Build Components
        uf = UnionFind(n)
        for u, v, w in edges:
            # union u and v as graph and see the connections from root
            uf.union(u, v)

        # 2. Get cost of each component (by and)
        component_cost = {}
        for u, v, w in edges:
            root = uf.find(u)
            # record root and if same means they are connected
            # use bitwize AND to find the minimum cost (e.g., 7 & 1 will be 1)
            if root not in component_cost:
                component_cost[root] = w
            else:
                component_cost[root] &= w


        # 3. Queries
        res = []

        for src, dst in query:
            r1, r2 = uf.find(src), uf.find(dst)
            if r1 != r2:
                res.append(-1) # parent node not the same, they are not connected
            else:
                res.append(component_cost[r1]) # same parent node, find the minimum cost
        return res

# time complexity: O(N + E + Q), where N is the number of nodes, E is the number of edges, and Q is the number of queries
# space complexity: O(N), where N is the number of nodes (for UnionFind parent and size arrays)