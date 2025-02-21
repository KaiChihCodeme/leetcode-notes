class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # cantor's diagonal argument: set of real numbers is uncountable; large infinite
        # there are different infinite sizes
        # no matter how list numbers, can always find one that is missing
        # basically idea is you have grid with all numbers from 0 to 1
        # then you construct a new number from diagonal. this number is not in grid
        # all unique since ith position from ith string means no other is taken from i,i
        ans = []
        # go across diagonal
        for i in range(len(nums)):
            curr = nums[i][i]
            # flip it
            ans.append("1" if curr == "0" else "0")
        
        return "".join(ans)
    
# time complexity: O(n)
# space complexity: O(n)
# a magic trick to solve this problem, wow