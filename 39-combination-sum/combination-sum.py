class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtracking(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            if total > target or i >= len(candidates):
                return

            curr.append(candidates[i])
            backtracking(i, curr, total + candidates[i])
            
            curr.pop()
            backtracking(i + 1, curr, total)

        backtracking(0, [], 0)
        return res