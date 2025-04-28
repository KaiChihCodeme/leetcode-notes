class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: x[0]) # sort by start time
        n = len(meetings)
        cnt = meetings[0][0]-1  # init from the day 1

        for i in range(1, n):
            # merge if overlay
            if meetings[i][0] <= meetings[i-1][1]:
                # check the last one must be the maximum
                # the minumum will always be true due to we use it to sort
                if meetings[i][1] < meetings[i-1][1]:
                    meetings[i][1] = meetings[i-1][1]
            else:
                # calculate the cnt
                cnt += meetings[i][0] - meetings[i-1][1] - 1

        # cal the last one
        cnt += days - meetings[n-1][1]
        
        return cnt

# time complexity: O(n log n) because sorting
# space complexity: O(1)