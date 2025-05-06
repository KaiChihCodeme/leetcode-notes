class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l, r = 0, len(matrix)-1

        while l < r:
            mid = l + (r-l) // 2
            min_range, max_range = matrix[mid][0], matrix[mid][-1]
            if target < min_range:
                r = mid - 1
            elif target > max_range:
                l = mid + 1
            elif min_range <= target and target <= max_range:
                l = mid
                break
        
        row_l, row_r = 0, len(matrix[l])-1

        while row_l <= row_r:
            mid = row_l + (row_r-row_l) // 2
            
            if target == matrix[l][mid]:
                return True
            elif target < matrix[l][mid]:
                row_r = mid-1
            else:
                row_l = mid+1
        
        return False

# # time complexity: O(log(m*n))
# # space complexity: O(1)