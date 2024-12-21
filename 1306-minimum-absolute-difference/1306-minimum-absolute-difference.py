class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        res = []
        min_diff = float("inf")

        for i in range(1, len(arr)):
            diff = abs(arr[i - 1] - arr[i])
            if diff < min_diff:
                min_diff = diff
                res = [[arr[i - 1], arr[i]]]
            elif diff == min_diff:
                res.append([arr[i - 1], arr[i]])

        return res
