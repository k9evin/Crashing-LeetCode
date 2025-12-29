# Last updated: 12/29/2025, 1:40:45 AM
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        def backtracking(track):
            if len(track) == len(nums):
                return track if track not in nums else None
            res = backtracking(track + '0')
            if res: 
                return res
            res = backtracking(track + '1')
            if res: 
                return res

        return backtracking('')
            
