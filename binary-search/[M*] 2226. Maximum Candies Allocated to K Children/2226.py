class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        l, r = 1, max(candies)
        ans = 0
        while l <= r:
            mid = l + (r - l) // 2

            cnt = 0
            for cand in candies:
                cnt += cand // mid

            if cnt >= k:
                ans = max(ans, mid)
                l = mid + 1
            else:
                r = mid - 1

        return ans

# time complexity: O(n * log(max(candies))), where n is the length of candies array
# space complexity: O(1), since we only use a few variables regardless of input size 
        

        
            

        