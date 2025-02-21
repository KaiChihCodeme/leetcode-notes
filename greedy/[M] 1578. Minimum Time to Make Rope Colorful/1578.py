class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        prev = 0
        res = 0
        for cur in range(1, len(colors)):
            if colors[cur] == colors[prev]:
                res += min(neededTime[cur], neededTime[prev])
                if neededTime[cur] >= neededTime[prev]:
                    prev = cur
            else:
                prev = cur
        
        return res

# time complexity: O(n)
# space complexity: O(1)

# that's greedy