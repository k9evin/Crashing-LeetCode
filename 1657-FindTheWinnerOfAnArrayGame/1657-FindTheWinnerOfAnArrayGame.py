# Last updated: 12/29/2025, 1:41:30 AM
class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        # initialize the current winner as the first number
        curr_winner = arr[0]
        win = 0

        for n in arr[1:]:
            # if the new number is larger, update the current winner and count
            if n > curr_winner:
                curr_winner = n
                win = 0

            # increment the win count if it is the same number
            win += 1

            # break out of the loop if reach k
            if win == k:
                break

        return curr_winner