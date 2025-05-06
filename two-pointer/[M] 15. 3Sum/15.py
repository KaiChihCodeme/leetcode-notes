class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 先排序，這樣才能使用two-pointer來對照到他的關係變化
        nums.sort()
        n, res = len(nums), []

        for i in range(n-1):
            # if nums[i] and nums[i-1] are same, skip due to result will be the same
            if i > 0 and nums[i] == nums[i-1]: 
                continue
            # only see the right side of the current number
            l, r = i+1, n-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                # if find sum is 0, then add to result
                if s == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    # move l backward
                    l += 1
                    # skip the same number to avoid duplicate result
                    while l<r and nums[l] == nums[l+1]: 
                        l+=1
                elif s < 0: 
                    # sum smaller than 0, move l forward
                    l += 1
                else: 
                    # sum larger than 0, move r backward
                    r -= 1
        
        return res
    
# # time complexity: O(n^2)
# # space complexity: O(N)
        