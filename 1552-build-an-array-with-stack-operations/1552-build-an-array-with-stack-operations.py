class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        # index of the target array
        index = 0

        # iterating the integers in the range [1, n]
        for n in range(1, target[-1] + 1):
            res.append('Push')
            # pop the integer from stack if it's not in target
            if n != target[index]:
                res.append('Pop')
            # else we have included a target integer
            else:
                index += 1
        
        return res