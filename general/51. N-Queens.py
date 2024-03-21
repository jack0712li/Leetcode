class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        chessBoard = ['.' * n for _ in range(n)]
        self.backTracking(n, 0, chessBoard, result)
        return result

    def backTracking(self, n, row, chessBoard, result):
        if row == n:
            result.append(chessBoard[:])
            return

        for col in range(n):
            if self.isValidate(row, col, chessBoard):
                chessBoard[row] = chessBoard[row][:col] + 'Q' + chessBoard[row][col+1:]
                self.backTracking(n, row+1, chessBoard, result)
                chessBoard[row] = chessBoard[row][:col] + '.' + chessBoard[row][col+1:]

    def isValidate(self, row, col, chessBoard):
        for i in range(row):
            if chessBoard[i][col] == 'Q':
                return False

        i, j = row-1, col-1
        while i >= 0 and j >= 0:
            if chessBoard[i][j] == 'Q':
                return False
            i -= 1
            j -= 1

        i, j = row-1, col+1
        while i >= 0 and j < len(chessBoard):
            if chessBoard[i][j] == 'Q':
                return False
            i -= 1
            j += 1

        return True