class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        l = len(cost)

        # cost[i] means the minimum cost to reach the i-th step
        # here will use back to front dp to avoid the cost of the space
        for i in range(l-3, -1, -1):
            cost[i] = cost[i] + min(cost[i+1], cost[i+2])

        return min(cost[0], cost[1])

# time complexity: O(n)
# space complexity: O(1)