class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_set = [set() for _ in range(len(board[0]))]
        row_set = [set() for _ in range(len(board))]
        box_set = [[set() for _ in range(len(board)//2)] for _ in range(len(board)//2)]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != '.':
                    # process col
                    if board[i][j] in col_set[i]:
                        return False
                    else:
                        col_set[i].add(board[i][j])

                    # process row
                    if board[i][j] in row_set[j]:
                        return False
                    else:
                        row_set[j].add(board[i][j])

                    # process box
                    if board[i][j] in box_set[i//3][j//3]:
                        return False
                    else:
                        box_set[i//3][j//3].add(board[i][j])

        return True
                    
# # time complexity: O(n^2)
# # space complexity: O(n)