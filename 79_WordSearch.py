class Solution(object):

    def searchBoard(self, row, col, count, trace):
        if count == len(self.word):
            self.state = True
            return self.state
        else:
            target = self.word[count]
            # left
            tr, tc = row, col - 1
            if tc >= 0:
                if target == self.board[tr][tc] and (tr, tc) not in trace:
                    self.searchBoard(tr, tc, count + 1, trace + [(tr, tc)])
            # right
            tr, tc = row, col + 1
            if tc < self.cols:
                if target == self.board[tr][tc] and (tr, tc) not in trace:
                    self.searchBoard(tr, tc, count + 1, trace + [(tr, tc)])
            # top
            tr, tc = row - 1, col
            if tr >= 0:
                if target == self.board[tr][tc] and (tr, tc) not in trace:
                    self.searchBoard(tr, tc, count + 1, trace + [(tr, tc)])
            # bottom
            tr, tc = row + 1, col
            if tr < self.rows:
                if target == self.board[tr][tc] and (tr, tc) not in trace:
                    self.searchBoard(tr, tc, count + 1, trace + [(tr, tc)])

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False
        else:
            self.state = False
            self.board = board
            self.rows = len(board)
            self.cols = len(board[0])
            self.word = word
            for r in xrange(self.rows):
                for c in xrange(self.cols):
                    if self.board[r][c] == word[0]:
                        self.searchBoard(r, c, 1, [(r, c)])
                        if self.state:
                            return True
            return False


if __name__ == '__main__':
    board = ["aa"]
    word = "aaa"
    solution = Solution()
    print solution.exist(board, word)
