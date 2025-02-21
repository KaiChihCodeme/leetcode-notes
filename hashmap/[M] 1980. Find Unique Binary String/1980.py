class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n_len = len(nums)
        dic = {}
        for i in range(2 ** n_len):
            binary_i = format(i, 'b')
            while len(binary_i) != n_len:
                binary_i = '0' + binary_i
            dic[binary_i] = False

        for j in nums:
            if j in dic:
                dic[j] = True

        for k, v in dic.items():
            if not v:
                return k

# time complexity: O(2^n)
# space complexity: O(2^n)