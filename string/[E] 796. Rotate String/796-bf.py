class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        # iterate all elements which fits the first element of s
        for i in range(len(goal)):
            if goal[i] == s[0]:
                g_ind = i
                ind = 0
                cnt = 0

                # using two pointers to check if the string is rotated
                while ind < len(s):
                    if s[ind] != goal[g_ind]:
                        break

                    if s[ind] == goal[g_ind]:
                        cnt += 1
                    if g_ind >= len(goal)-1:
                        g_ind = 0
                    else:
                        g_ind += 1
                    ind += 1
                
                # if we found the rotated string, return True
                if cnt == len(s):
                    return True

        return False

# time complexity: O(n^2)
# space complexity: O(1)

# this is a worse solution with longer runtime 