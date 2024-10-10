class Solution:
    def shipWithinDays(self, weights, D):
        # capacity will be in the range of max(weights) to sum(weights), so we can use binary search to find the capacity
        left, right = max(weights), sum(weights)
        while left < right:
            mid, need, cur = (left + right) / 2, 1, 0
            # iterately to calculate the need of capacity from weights
            for w in weights:
                if cur + w > mid:
                    need += 1
                    cur = 0
                cur += w
                
            # if need days > days (which calculating by mid), that means capacity is not enough in mid capacity. 
            # So we need to increase the capacity uppper than mid, so left would be mid + 1
            if need > D: 
                left = mid + 1
            else: 
                # else, we can decrease the capacity to find the minimum capacity, so right would be mid1
                right = mid
        # return the left value because left is the minimum capacity
        return left
    
# time complexity: O(nlogn), n is the length of weights
# space complexity: O(1)