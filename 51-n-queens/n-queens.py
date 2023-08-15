class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        col = set()
        # points that are diagonal have the same
        posDiag = set() # (r + c)
        negDiag = set() # (r - c)

        # create the board with '.'
        board = [["."] * n for _ in range(n)]

        def backtrack(row: int):
            # if we finish all the rows
            if row == n:
                res.append(["".join(row) for row in board])
                return
            
            # for all the columns in a row
            for column in range(n):
                # if current column or diagonals has a queen already
                if (column in col or 
                   (row + column) in posDiag or 
                   (row - column) in negDiag):
                    continue
                # mark current position as queen
                col.add(column)
                posDiag.add(row + column)
                negDiag.add(row - column)
                board[row][column] = "Q"
                # backtrack to next row
                backtrack(row + 1)
                # remove queen from current position
                col.remove(column)
                posDiag.remove(row + column)
                negDiag.remove(row - column)
                board[row][column] = "."
        
        # start backtracking from the first row
        backtrack(0)
        return res