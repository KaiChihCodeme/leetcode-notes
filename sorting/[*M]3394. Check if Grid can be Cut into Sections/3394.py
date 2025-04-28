class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        def check(interval):
            interval.sort()
            section = 0
            max_end = interval[0][1]

            # if there is no overlap, it can be a valid rectangle
            for start, end in interval:
                if max_end <= start:
                    section += 1
                max_end = max(end, max_end)
            
            # because we need at least 2 non-overlapping sections for two cut
            return section >= 2

        # check if we can cut vertically or horizontally
        x_interval = [[i[0], i[2]] for i in rectangles]
        y_interval = [[j[1], j[3]] for j in rectangles]

        # reach answer if any direction works
        return check(x_interval) or check(y_interval)
    
## time complexity: O(NlogN) where N is the number of rectangles (for sorting)
# space complexity: O(N) where N is the number of rectangles (for storing intervals)


