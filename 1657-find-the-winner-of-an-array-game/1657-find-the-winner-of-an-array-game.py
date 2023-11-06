class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        curr_winner = arr[0]
        win = 0

        for n in arr[1:]:
            if n > curr_winner:
                curr_winner = n
                win = 0

            win += 1
            
            if win == k:
                break

        return curr_winner