class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # Adjacency lists for each vertex
        graph = defaultdict(list)

        # Build adjacency lists from edges
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)

        complete_count = 0
        visited = set()

        def _dfs(curr: int, info: list) -> None:
            visited.add(curr)
            info[0] += 1  # Increment vertex count
            info[1] += len(graph[curr])  # Add edges from current vertex

            # Explore unvisited neighbors
            for next_vertex in graph[curr]:
                if next_vertex not in visited:
                    _dfs(next_vertex, info)

        # Process each unvisited vertex
        for vertex in range(n):
            if vertex in visited:
                continue

            # info[0] = vertices count, info[1] = total edges count
            component_info = [0, 0]
            _dfs(vertex, component_info)

            # Check if component is complete - edges should be vertices * (vertices-1)
            if component_info[0] * (component_info[0] - 1) == component_info[1]:
                complete_count += 1

        return complete_count

# time complexity: O(V + E) where V is the number of vertices and E is the number of edges
# space complexity: O(V) where V is the number of vertices, as we need a visited set and recursion stack