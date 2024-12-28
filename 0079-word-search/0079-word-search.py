class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def dfs(r, c, i):
            # If we reach the length of the word, we find the word
            if i == len(word):
                return True
            # Check for boundry, repeated character, and if the current
            # character is what we are looking for
            if (
                r < 0
                or r >= m
                or c < 0
                or c >= n
                or board[r][c] != word[i]
                or board[r][c] == "#"
            ):
                return False

            # Mark the current character as visited
            board[r][c] = "#"
            # Check if we can find the remaining character from here
            res = (
                dfs(r + 1, c, i + 1)
                or dfs(r - 1, c, i + 1)
                or dfs(r, c + 1, i + 1)
                or dfs(r, c - 1, i + 1)
            )
            # Unmark the current character to its original
            board[r][c] = word[i]
            return res

        for r in range(m):
            for c in range(n):
                # If dfs(r, c, 0) returns true, we have the whole word in board
                if dfs(r, c, 0):
                    return True
        return False
