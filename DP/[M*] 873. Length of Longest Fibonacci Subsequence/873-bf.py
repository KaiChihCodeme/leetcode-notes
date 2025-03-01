class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        s = set(arr)
        res = 2

        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                a, b, l = arr[i], arr[j], 2
                while a+b in s:
                    a, b, l = b, a+b, l+1
                res = max(res, l)
        
        return res if res > 2 else 0

# time complexity: O(n^2 * log(max(arr)))
# space complexity: O(N) since we only use a set to store the array elements
# the concept can be figured out by me but hard to turn into code. I should practice more to implement the 
# brute force and my thought smoothly.