class Solution:
    def lastRemaining(self, n: int) -> int:
        def process(n, is_backward):
            if n == 1:
                return 1

            if is_backward:
                return 2 * process(n // 2, False)
            elif n % 2 == 1:
                return 2 * process(n // 2, True)
            else:
                # not backward and n % 2 == 0
                return 2 * process(n // 2, True) - 1

        return process(n, True)

# Time complexity: O(logn)
# Space complexity: O(logn)