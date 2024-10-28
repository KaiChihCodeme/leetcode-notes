class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        # Start from (1,1), due to we don't need to check the first row and first column, it only has one possible square
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                # we just need to check the left, top, and top-left element, and add 1 to the minimum value of them
                # and if current is 0, then it is impossible to form a square, so we use multiply to set it to 0
                matrix[i][j] *= min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]) + 1
        
        # add all posible squares
        return sum(map(sum, matrix))
    
# time complexity: O(n*m), n is the number of rows, m is the number of columns
# space complexity: O(1), we don't use extra space