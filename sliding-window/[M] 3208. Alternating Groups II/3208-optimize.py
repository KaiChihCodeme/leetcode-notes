class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int: 
        n = len(colors)
        count = 0
        left = 0

        for right in range(n + k - 1):
            if right > 0 and colors[right % n] == colors[(right - 1) % n]:
                left = right  
            
            if right - left + 1 >= k:
                count += 1  
        
        return count
    
# time complexity: O(n), where n is the length of the colors array
# space complexity: O(1), as we only use a few variables regardless of input size
# this solution like extend array from for loop range, then check if there has duplicated, just move left to right index
# and count+=1 if r-l+1 >= k means we found it.
# ref: https://leetcode.com/problems/alternating-groups-ii/solutions/6515222/sliding-window-python-c-java-js-c-go-swift-rust