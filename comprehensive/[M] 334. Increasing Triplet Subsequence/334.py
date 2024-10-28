class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float('inf')

        for i in nums:
            # find the smallest number
            if i <= first:
                first = i
            # find the second smallest number, but need to greater than first number
            elif i <= second:
                second = i
            # if we find a number greater than second, we find the increasing triplet
            else:
                return True
        return False

# Time complexity: O(n)
# Space complexity: O(1)