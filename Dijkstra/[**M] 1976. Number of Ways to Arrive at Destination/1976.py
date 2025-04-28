class Solution:
    def countPaths(self, n, roads):
        G = defaultdict(list)
        for x, y, w in roads:
            G[x].append((y, w))
            G[y].append((x, w))

        dist = [float('inf')] * n
        dist[0] = 0
        cnt = [0]*n
        cnt[0] = 1
        heap = [(0, 0)]

        # This is a standard Dijkstra's algorithm implementation
        while heap:
            (min_dist, idx) = heappop(heap)
            # reach the target, return count
            if idx == n-1: return cnt[idx] % (10**9 + 7)
            for neib, weight in G[idx]:
                candidate = min_dist + weight
                # if candidate is the shoretest path to neib, add the count from idx
                if candidate == dist[neib]:
                    cnt[neib] += cnt[idx]

                # update the shortest path, and update this node into heap
                elif candidate < dist[neib]:
                    dist[neib] = candidate
                    heappush(heap, (weight + min_dist, neib))
                    cnt[neib] = cnt[idx]

# time complexity: O(E * log V) where E is the number of edges and V is the number of vertices
# space complexity: O(V) for the dist and cnt arrays and heap