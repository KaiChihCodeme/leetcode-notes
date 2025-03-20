class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        temp =0
        l=0
        result=0
        n=len(nums)
        for r,num in enumerate(nums):
            while num&temp:
                temp^=nums[l]
                l+=1
            result=max(result,r-l+1)
            temp|=num
        return result

# time complexity: O(n)
# space complexity: O(1)
# this is a bitwise solution