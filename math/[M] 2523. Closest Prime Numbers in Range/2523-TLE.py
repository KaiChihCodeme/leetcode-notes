class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        primes_list = []
        # create a prime list between left and right
        for cur in range(left, right+1):
            half = (cur // 2) +1
            # check if prime
            is_prime = True
            for i in range(2, half+1):
                if cur % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes_list.append(cur)

        if len(primes_list) < 2:
            return [-1, -1]
        
        # process min difference between two consecutive primes
        ans = [primes_list[0], primes_list[1]]
        cur_min = primes_list[1]-primes_list[0]
        for j in range(1, len(primes_list)-1):
            diff = primes_list[j+1]-primes_list[j]
            if diff < cur_min:
                cur_min = diff
                ans[0], ans[1] = primes_list[j], primes_list[j+1]

        return ans
    
# time complexity: O(N^2)
# space complexity: O(N)
# this solution will TLE.
