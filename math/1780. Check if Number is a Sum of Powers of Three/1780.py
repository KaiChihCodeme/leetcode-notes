class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        max_n = 0
        while 3 ** max_n <= n:
            if 3 ** max_n == n:
                return True
            
            max_n += 1
        
        # all possible set
        pl = [[]]
        for num in range(max_n):
            pl += [cur+[3**num] for cur in pl]

        for pos in pl:
            if sum(pos) == n:
                return True

        return False

# time complexity: O(2^n), where n is the number of powers of three less than or equal to the input number
# space complexity: O(2^n), where n is the number of powers of three less than or equal to the input number