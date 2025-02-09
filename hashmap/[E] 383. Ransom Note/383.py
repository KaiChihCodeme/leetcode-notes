class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m = {}

        for i in magazine:
            if i not in m:
                m[i] = 1
            else:
                m[i] += 1

        for j in ransomNote:
            if j in m and m[j] > 0:
                m[j] -= 1
            else:
                return False

        return True

# time complexity: O(n)
# space complexity: O(n)