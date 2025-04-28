class Solution:
    def countDays(self, days: int, meetings: list[list[int]]) -> int:
        free_days = 0
        latest_end = 0

        # Sort meetings based on starting times
        meetings.sort()

        for start, end in meetings:
            # Add current range of days without a meeting
            if start > latest_end + 1:
                free_days += start - latest_end - 1

            # Update latest meeting end
            latest_end = max(latest_end, end)

        # Add all days after the last day of meetings
        free_days += days - latest_end

        return free_days

# time complexity: O(n log n) where n is the length of meetings array, due to sorting
# space complexity: O(1) as we only use a few variables regardless of input size
# or O(N) for sorting