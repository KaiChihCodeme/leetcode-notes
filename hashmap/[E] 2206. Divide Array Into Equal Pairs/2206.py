class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        dic = collections.defaultdict(int)

        for i in nums:
            dic[i] += 1

        n_pair = len(nums) / 2
        
        cnt = 0
        for v in dic.values():
            if v % 2 != 0:
                return False
            cnt += (v/2)
        
        return cnt == n_pair
# time complexity: O(n)
# space complexity: O(n) 
            
            