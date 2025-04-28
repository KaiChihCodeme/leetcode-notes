class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        tmp_l = [0] * days
        for i in meetings:
            for j in range(i[0], i[1]+1):
                tmp_l[j-1] = 1

        cnt = 0
        for k in tmp_l:
            if k == 0:
                cnt += 1

        return cnt 

# time complexity: O(n * m) where n is the number of days and m is the number of meetings
# space complexity: O(n) where n is the number of days