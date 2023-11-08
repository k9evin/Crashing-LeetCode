class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if fx == sx and fy == sy and t == 1:
            return False

        return t >= max(abs(fx - sx), abs(fy - sy))