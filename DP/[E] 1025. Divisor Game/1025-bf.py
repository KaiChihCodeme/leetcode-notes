class Solution:
    def divisorGame(self, n: int) -> bool:
        rnd = 0

        while True:
            found = False
            for step in range(1, n):
                if n % step == 0:
                    n = n - step
                    rnd += 1
                    found = True
                    break

            # not fit rules
            if not found:
                break
        
        # if this round is not even, then Alice wins, because we always stop at failure round
        # Alice represents even round, Bob represents odd
        return rnd % 2 != 0
        

# Time complexity: O(n^2)
# Space complexity: O(1)