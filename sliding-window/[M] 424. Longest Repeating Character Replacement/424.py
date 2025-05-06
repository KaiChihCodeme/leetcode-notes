class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # using sliding window (start, end) to find the longest substring
        # and we need to record the maximum character, and we minus it will get the expected replacement numbers
        # res will store the longest substring length
        start, max_cnt, res = 0, 0, 0
        cnt_dic = collection.defaultdict(int)
        
        # we use iterate s to get end index
        for end in range(len(s)):
            # update the count of current character
            cnt_dic[s[end]] += 1
            max_cnt = max(max_cnt, cnt_dic[s[end]])
            
            # end-start = sliding window, and - max_cnt, we will get the expected replacement numbers
            if end - start - max_cnt < k:
                # if the expected replacement numbers is less than k, we can keep the current substring
                res += 1
            else:
                # else, we need to move the start index forward
                # remove from cnt_dic at first due to we move forward
                cnt_dic[s[start]] -= 1
                start += 1
                
        return res
    
# # time complexity: O(n)
# # space complexity: O(N)