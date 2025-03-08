class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        primes_list = []
        cur_min = float('inf')
        ans = []
        for cur in range(left, right+1):
            is_prime = True
            # process special rule of 1 and 2 and others
            if cur == 1:
                is_prime = False
            elif cur == 2:
                is_prime = True
            else:
                half = (cur // 2) +1
                # check if prime
                
                for i in range(2, half+1):
                    if cur % i == 0:
                        is_prime = False
                        break
            # if prime, calculate diff with previous one if exists.
            # A special rule to avoid to TLE is if diff <= 2, it will be answer by math
            if is_prime:
                if len(primes_list) > 0:
                    diff = cur-primes_list[-1]
                    if diff <= 2:
                        return [primes_list[-1], cur]
                    
                    if diff < cur_min:
                        cur_min = diff
                        ans = [primes_list[-1], cur]
                    
                primes_list.append(cur)

        if len(primes_list) < 2:
            return [-1, -1]

        return ans

# time complexity: O((right - left) * sqrt(right)) (N^2, but calculate diff when find prime, and return directly when diff<=2)
# space complexity: O(right - left) (O(N), store prime numbers in list)