class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        counter=collections.Counter(nums)
        for count in counter.values():
            if count%2 == 1: # if odd
                return False
        
        return True