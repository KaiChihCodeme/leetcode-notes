class Solution:
    def longestSquareStreak(self, nums):
        mp = {}
        # must sort, then we are able to check by np
        nums.sort()
        res = -1

        for num in nums:
            # get the square root of the number (int)
            sqrt = isqrt(num)

            # if the square of the square root is the same as the number, and the square root is in the map, then add 1
            # and get the max
            if sqrt * sqrt == num and sqrt in mp:
                mp[num] = mp[sqrt] + 1
                res = max(res, mp[num])
            # if not, then add the number to the map with 1
            else:
                mp[num] = 1

        return res
    
# Time Complexity: O(nlogn)
# Space Complexity: O(n)

# e.g., [4, 3, 6, 16, 8, 2] -> [2, 3, 4, 6, 8, 16]
# {2: 1, 3: 1, 4: 1+1=2, 6: 1, 8: 1, 16: 2+1=3}