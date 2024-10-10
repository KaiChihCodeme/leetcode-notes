class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # This is a formal solution, which r will be the last index
        l, r = 0, len(nums)-1
        while l < r:
            mid = l + (r - l) // 2 # avoid overflow, which is same as (l+r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        
        if nums[l] < target:
            # nums[l] smaller than target, target need to insert after nums[l]
            return l+1
        else:
            # nums[l] greater than target, target do not need to change position
            return l