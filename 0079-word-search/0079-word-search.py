class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Algorithm:
        - Perform a Depth-First Search (DFS) for each cell in the board to find the first character of the word.
        - If a match is found, recursively search for the next character in the four possible directions.
        - Use backtracking by marking visited cells to avoid reusing characters.
        - Unmark the visited cells after exploring all paths.

        Time Complexity: O(m * n * 4^L), where m and n are the dimensions of the board, and L is the length of the word.
                         Each cell is visited, and for each cell, we explore up to 4 directions up to the length of the word.
        Space Complexity: O(L), where L is the length of the word, for the recursion stack.
        """

        rows, cols = len(board), len(board[0])  # Dimensions of the board

        def dfs(row: int, col: int, index: int) -> bool:
            """
            Depth-First Search to check if the word can be formed starting from (row, col).
            """
            # Base case: All characters in the word are found
            if index == len(word):
                return True

            # Out of bounds, mismatched character, or already visited
            if (
                row < 0
                or row >= rows
                or col < 0
                or col >= cols
                or board[row][col] != word[index]
                or board[row][col] == "#"
            ):
                return False

            # Mark the current cell as visited
            original_char = board[row][col]
            board[row][col] = "#"

            # Explore all 4 possible directions
            found = (
                dfs(row + 1, col, index + 1)  # Down
                or dfs(row - 1, col, index + 1)  # Up
                or dfs(row, col + 1, index + 1)  # Right
                or dfs(row, col - 1, index + 1)  # Left
            )

            # Backtrack: Restore the original character
            board[row][col] = original_char

            return found

        # Try to find the word starting from each cell in the board
        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0):  # Start DFS from this cell
                    return True

        return False  # Return false if no match is found
