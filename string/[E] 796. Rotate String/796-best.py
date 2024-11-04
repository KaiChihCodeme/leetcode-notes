class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)):
            if s[i:] + s[:i] == goal:
                return True
        return False

# time complexity: O(n^2), due to the string concatenation and compare to goal is O(n)
# space complexity: O(n)

# but this is a better solution with shorter runtime