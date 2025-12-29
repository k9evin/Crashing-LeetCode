# Last updated: 12/29/2025, 1:40:30 AM
class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        # no matter which types of garbage, they all take 1 unit to collect
        total_time = sum(len(g) for g in garbage)
        travel = [0] + travel

        # python evaluates false as 0 and true as 1, so we can use this to indicate the existance of the garbage
        G, P, M = False, False, False
        for i in range(len(travel) - 1, -1, -1):
            G |= 'G' in garbage[i]
            P |= 'P' in garbage[i]
            M |= 'M' in garbage[i]

            total_time += travel[i] * (G + P + M)

        return total_time