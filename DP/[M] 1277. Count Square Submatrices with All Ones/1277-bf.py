class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        #1: every 1
        #2: same y axis should the same for 2, and two x axis
        #3: same y axis should the same for 3, and three x axis

        cnt = 0

        # iterate check the n size of square
        n = 1
        # within matrix size
        while True and n <= len(matrix):
            # iterate all elements in the matrix
            for x in range(len(matrix)):
                for y in range(len(matrix[x])):
                    is_square = True
                    
                    # check out the square with size n
                    for i in range(n):
                        for j in range(n):
                            # if out of bound or the element is 0, then it is not a square, break all checking loops
                            if x+i > len(matrix)-1 or y+j > len(matrix[0])-1 or matrix[x+i][y+j] == 0:
                                is_square = False
                                break
                        if not is_square:
                            break
                    if is_square:
                        cnt += 1
            n += 1

        return cnt

# Time complexity: O(n^3), n is the number of rows or columns
# Space complexity: O(1), we don't use extra space