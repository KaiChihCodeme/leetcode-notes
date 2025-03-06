class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left_list = []
        middle_list = []
        right_list = []

        for i in nums:
            if i < pivot:
                left_list.append(i)
            elif i == pivot:
                middle_list.append(i)
            else:
                right_list.append(i)

        return left_list+middle_list+right_list

# time complexity: O(n)
# space complexity: O(n)