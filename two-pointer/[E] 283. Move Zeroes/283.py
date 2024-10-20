class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, len(nums)
        while i < j:
            if nums[i] != 0:
                i += 1
                continue

            if nums[i] == 0:
                nums.append(nums[i])
                nums.pop(i)
                j -= 1

        return nums

# TC: O(n)
# SC: O(1)