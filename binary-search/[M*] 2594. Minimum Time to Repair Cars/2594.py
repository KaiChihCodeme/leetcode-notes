class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        # at least maximum we can find is min(ranks)*cars*cars
        l, r = 0, min(ranks) * cars * cars

        while l < r:
            mid = l + (r - l) // 2

            cnt = 0
            # calculate cars we can repair by this mid time
            for i in ranks:
                cnt += int(math.sqrt(mid / i))
            
            # it we can repair >= cars, update r. instead, update l.
            if cnt >= cars:
                r = mid
            else:
                l = mid + 1

        return l

# time complexity: O(NlogN)
# space complexity: O(1)
# Almost solve it!