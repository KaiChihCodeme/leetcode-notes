class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        tmp = []
        
        # e.g., if k>len(nums), such as [-1] and k=2, then the init index whould be (2%1)*-1 = -1
        init_ind = (k % len(nums)) * -1

        original_len = len(nums)
        while len(tmp) < original_len:
            tmp.append(nums[init_ind])
            init_ind += 1

        # copy the tmp list to the original list
        nums[:] = tmp[:]

# time complexity: O(n)
# space complexity: O(n)