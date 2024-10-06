class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        # player1 should better or equal to player2
        return self.recursion(nums, 0, len(nums)-1) >= 0

    def recursion(self, nums, l, r):
        # stop condition
        if l == r:
            return nums[l]

        # pick the best choice for cuurent player
        return max(nums[l]-self.recursion(nums,l+1, r), nums[r]-self.recursion(nums, l, r-1))
    
    # TC: O(2^n) [tree-like situation], SC: O(N)