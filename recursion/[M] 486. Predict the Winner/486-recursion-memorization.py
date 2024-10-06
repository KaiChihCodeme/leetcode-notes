class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        self.dic = {}
        return self.recursion(nums, 0, len(nums)-1) >= 0

    def recursion(self, nums, l, r):
        if l == r:
            return nums[l]

        # do memorization, calculate the key for the same l, r pair
        k = l * len(nums) + r

        if self.dic.get(k) is None:
            self.dic[k] = max(nums[l]-self.recursion(nums,l+1, r), nums[r]-self.recursion(nums, l, r-1))


        return self.dic[k]
    
    # TC: O(N^2), SC: O(N^2)