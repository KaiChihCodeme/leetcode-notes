class Solution:
    def lastRemaining(self, n: int) -> int:
        arr = [i+1 for i in range(n)]
        return self.process(arr, True)

    def process(self, arr, is_backward):
        if len(arr) == 1:
            return arr[0]

        new_backward = False

        if is_backward:
            ind = 1
            new_arr = []
            while ind < len(arr):
                new_arr.append(arr[ind])
                ind += 2
        else:
            ind = len(arr)-2
            new_arr = []
            while ind >= 0:
                new_arr.append(arr[ind])
                ind -= 2
            new_arr[:] = new_arr[::-1]
            new_backward = True
        
        return self.process(new_arr, new_backward)
            

# Time complexity: O(n)
# Space complexity: O(n)