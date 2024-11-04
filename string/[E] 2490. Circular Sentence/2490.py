class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split(" ")

        for i in range(1, len(words)):
            if words[i-1][-1] != words[i][0]:
                return False

        if words[-1][-1] != words[0][0]:
            return False

        return True

# time complexity: O(n)
# space complexity: O(n)