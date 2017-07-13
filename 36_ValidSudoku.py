class Solution(object):

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for row in board:
            temp_dict = {}
            for col in row:
                if col in temp_dict and col != '.':
                    return False
                if col not in temp_dict:
                    temp_dict[col] = 0

        rev_board = zip(*board)
        for row in rev_board:
            temp_dict = {}
            for col in row:
                if col in temp_dict and col != '.':
                    return False
                if col not in temp_dict:
                    temp_dict[col] = 0

        for i in xrange(len(board) / 3):
            for j in xrange(len(board) / 3):
                temp = board[i * 3][j * 3:j * 3 + 3] +\
                    board[i * 3 + 1][j * 3:j * 3 + 3] +\
                    board[i * 3 + 2][j * 3:j * 3 + 3]
                temp_dict = {}
                for k in temp:
                    if k in temp_dict and k != '.':
                        return False
                    if k not in temp_dict:
                        temp_dict[k] = 0
        return True
