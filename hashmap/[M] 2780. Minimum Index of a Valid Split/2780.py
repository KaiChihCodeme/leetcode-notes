class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        # find the max cnt number
        cnt_dic = collections.Counter(nums)
        max_number = -1
        max_cnt_key = -1
        for k, v in cnt_dic.items():
            if v > max_number:
                max_number = v
                max_cnt_key = k
        
        # calculate index
        index = 0
        cur_cnt = 0
        while index < len(nums):
            if nums[index] == max_cnt_key:
                cur_cnt += 1
            
                if cur_cnt * 2 > index+1 and (max_number-cur_cnt) * 2 > len(nums)-(index+1):
                    return index
            index += 1
        return -1

# time complexity: O(n) where n is the length of nums
# space complexity: O(n) where n is the length of nums (for storing the counter dictionary)