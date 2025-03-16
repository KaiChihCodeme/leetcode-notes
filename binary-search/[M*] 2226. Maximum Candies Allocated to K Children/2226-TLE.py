class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        total_sum = 0
        for i in candies:
            total_sum += i

        if total_sum < k:
            return 0

        ind = max(candies)
        if k == 1:
            return ind

        # Here process too many times
        while ind > 0:
            cnt = 0
            for j in candies:
                cnt += j // ind
            if cnt >= k:
                return ind
            ind -= 1
        
# time complexity: O(max(candies) * n), where n is the length of candies array
# space complexity: O(1), since we only use a few variables regardless of input size
        

        
            

        